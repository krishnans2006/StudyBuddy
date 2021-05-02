from discord.ext import commands
from helpers.funcs import create_embed, get_reacts, check
from models.classModels import Class, Task, Exam, User

import datetime


c_daysList = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

class Setup(commands.Cog, name="setup", description="Set up the bot and personalize it to your schedule!"):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name="new-class", brief="Create a class", description="Create a class to add to your schedule, or to publish and share to your students!")
    async def newclass(self, context):
        embed = create_embed(
            "Create a class!",
            description="To create a class, first choose whether you are creating this class for yourself or as a teacher. If you are creating this as a teacher, you will be provided with a class code to share with your students.",
            fields=[
                ["As a Teacher", "React with 👨‍🏫", True],
                ["For Yourself", "React with 👨‍🎓", True]
            ]
        )
        message = await context.send(embed=embed)
        react = await get_reacts(context, self.client, message, ["👨‍🏫", "👨‍🎓"])
        current = Class()
        if react.emoji == "👨‍🏫":
            current.teacher = context.author.id
            current.subject = current.teacher
        elif react.emoji == "👨‍🎓":
            embed = create_embed(
                "Moving on...",
                description="Now, tell me the name of the teacher who is teaching this class. Just type it in below:"
            )
            message = await context.send(embed=embed)
            resp = await self.client.wait_for("message", check=check(context.author, context.channel))
            current.teacher = resp.content
            current.subject = current.teacher
        else:
            raise Exception("You've broken Python!")
        
        embed = create_embed(
            "Perfect! Let's keep going...",
            description="Now, set your class name. This is what you will use to add Tasks and Exams, and to reference it later. Just type it in below:"
        )

        message = await context.send(embed=embed)
        resp = await self.client.wait_for("message", check=check(context.author, context.channel))
        current.name = resp.content
        embed = create_embed(
          f'{current.name} is your class',
          description = "Is this correct?"
        )
        message = await context.send(embed=embed)
        react = await get_reacts(context, self.client, message, ["❌", "✅"])
        while(react.emoji=="❌"):
          embed = create_embed(
            #Maybe 'your' name? If its the teacher??
            "Please enter the class's name: "
          )
          message = await context.send(embed=embed)
          resp = await self.client.wait_for("message", check=check(context.author, context.channel))
          current.name = resp.content
          embed = create_embed(
            f'{current.name} is your class name',
            description = "Is this correct?"
          )
          message = await context.send(embed=embed)
          react = await get_reacts(context, self.client, message, ["❌", "✅"])


        embed = create_embed(
          f"Now, we need the information for {current.name}'s schedule",
          description=f"Please enter the hours that {current.name} will meet"
        )
        message = await context.send(embed=embed)
        index = 0
        for item in current.days:
            message = await context.send(f"Please enter times for {c_daysList[index]}! If the class doesn't meet on that day, enter anything that's not two numbers separated by a `-`.")
            resp = await self.client.wait_for("message", check=check(context.author, context.channel))
            try:
                resp = resp.content
                if not "-" in resp:
                    raise Exception("Nope")
                current.days[index]=str(resp)
                index += 1
            except Exception as e:
                index += 1
        current.at = current.days
        embed = create_embed(
          "Almost done! The last thing to do is to enter a description of the class"
        )
        message = await context.send(embed=embed)
        resp = await self.client.wait_for("message", check=check(context.author, context.channel))
        current.description = resp.content
        embed = create_embed(
            "Is this correct?",
            fields=[
                ["Teacher", "You" if isinstance(current.teacher, int) else current.teacher, True],
                ["Name", current.name, True],
                ["Description", current.description, True],
                ["Meeting Times", ", ".join([c_daysList[i] + ": " + current.days[i] for i in range(7)])]
            ]
        )
        message = await context.send(embed=embed)
        react = await get_reacts(context, self.client, message, ["✅", "❌"])
        if react.emoji == "✅":
            await context.send("Successfully added class!")
        elif react.emoji == "❌":
            await context.send("Cancelled adding class!")
        else:
            raise Exception("You've broken Python!")
    
    @commands.command(name="join-class", brief="Join a class", description="Join a class with a join code")
    async def joinclass(self, context):
        await context.send("Enter the join code provided by your teacher! (Example: `783465`)")
        resp = await self.client.wait_for("message", check=check(context.author, context.channel))
        class React:
            emoji = "❌"
        react = React()
        while(react.emoji=="❌"):
            code = int(resp.content)
            embed = create_embed(
                "Are you sure?",
                description="Are you sure you want to join this class? ✅ or ❌",
                fields=[
                    ["Class", "Biology Honors"],
                    ["Description:", "Bio Honors Period 4! Room 68, Second Floor. Have fun learning Biology!"],
                    ["Teacher", "Mr. Jeff", True],
                    ["Meeting Times", "Monday: 2-3:30, Tuesday: 4-5, Wednesday: 2-3:30, Thursday: 4-5, Friday: 2-3:30"]
                ]
            )
            message = await context.send(embed=embed)
            react = await get_reacts(context, self.client, message, ["✅", "❌"])
            if react.emoji == "✅":
                await context.send("Successfully joined class!")
            elif react.emoji == "❌":
                await context.send("Cancelled joining class!")
            else:
                raise Exception("You've broken Python!")
            #await context.send("Invalid code! Please enter a valid code")#do we want to keep this?
    
    @commands.command(name='new-task', brief="Create a new task", description="Create a new task for your class!")
    async def newtask(self, context):
        embed = create_embed(
            "Time to make a new Task!",
            description="Which class is this task for?\n\nYour classes: `Science`, `History`, `English`, `Math`, `Tech`, `Spanish`, and `Computer Science`"
        )
        await context.send(embed=embed)
        current = Task()
        subject = await self.client.wait_for("message", check=check(context.author, context.channel))
        current.subject = subject.content
        embed=create_embed(
            f"New Task for {current.subject}",
            description="Please enter the task name!"
        )
        message = await context.send(embed=embed)
        resp = await self.client.wait_for("message", check=check(context.author, context.channel))
        current.name = resp.content
        embed=create_embed(
            f"New Task: {current.name}",
            description="A description of this task (optional)"
        )
        message = await context.send(embed=embed)
        resp = await self.client.wait_for("message", check=check(context.author, context.channel))
        current.description = resp.content
        while True:
            embed=create_embed(
                f"New Task: {current.name}",
                description="When is this task at? Format: mm/dd/yy\nExample: `03/09/21`."
            )
            message = await context.send(embed=embed)
            resp = await self.client.wait_for("message", check=check(context.author, context.channel))
            resp = resp.content.split("/")
            if len(resp) == 3 and all(len(x) == 2 for x in resp):
                try:
                    for x in range(len(resp)):
                        resp[x] = int(resp[x])
                    current.dueDate = datetime.date(resp[2], resp[0], resp[1])
                    current.at = current.dueDate
                    break
                except Exception as e:
                    print(e)
                    await context.send("Invalid Date!")
            else:
                await context.send("Invalid Date!")
        embed = create_embed(
            f"Task: {current.name}",
            description="Is this correct? ✅ or ❌",
            fields=[
                ["Description", current.description],
                ["Subject", current.subject, True],
                ["At", current.dueDate.strftime("%A %B %d, %Y (%m/%d/%y)"), True]
            ]
        )
        message = await context.send(embed=embed)
        react = await get_reacts(context, self.client, message, ["✅", "❌"])
        if react.emoji == "✅":
            await context.send("Successfully added task!")
        elif react.emoji == "❌":
            await context.send("Cancelled adding task!")
        else:
            raise Exception("You've broken Python!")

    @commands.command(name='new-exam', brief="Create a new exam", description="Create a new exam for your class!")
    async def newexam(self, context):
        embed = create_embed(
            "Time to make a new Exam!",
            description="Which class is this exam for?\n\nYour classes: `Science`, `History`, `English`, `Math`, `Tech`, `Spanish`, and `Computer Science`"
        )
        await context.send(embed=embed)
        current = Exam()
        subject = await self.client.wait_for("message", check=check(context.author, context.channel))
        current.subject = subject.content
        embed=create_embed(
            f"New Exam for {current.subject}",
            description="Please enter the exam name!"
        )
        message = await context.send(embed=embed)
        resp = await self.client.wait_for("message", check=check(context.author, context.channel))
        current.name = resp.content
        embed=create_embed(
            f"New Exam: {current.name}",
            description="A description of this exam (optional)"
        )
        message = await context.send(embed=embed)
        resp = await self.client.wait_for("message", check=check(context.author, context.channel))
        current.description = resp.content
        while True:
            embed=create_embed(
                f"New Exam: {current.name}",
                description="When is this exam at? Format: mm/dd/yy hh:mm AM/PM\nExample: `03/09/21 3:45 PM`."
            )
            message = await context.send(embed=embed)
            resp = await self.client.wait_for("message", check=check(context.author, context.channel))
            resp = resp.content.split("/")
            if len(resp) == 3:
                try:
                    endsplit = resp[2].split(" ")
                    resp[2] = endsplit[0]
                    t = endsplit[1].split(":")
                    if len(t) == 2 and all(len(x) == 2 for x in resp):
                        for x in range(len(resp)):
                            resp[x] = int(resp[x])
                        for x in range(len(t)):
                            t[x] = int(t[x])
                        if endsplit[2].lower() == "pm":
                            t[0] += 12
                        current.date = datetime.datetime(resp[2], resp[0], resp[1], t[0], t[1])
                        current.at = current.date
                        break
                except Exception as e:
                    print(e)
                    await context.send("Invalid Date!")
            else:
                await context.send("Invalid Date!")
        embed = create_embed(
            f"Exam: {current.name}",
            description="Is this correct? ✅ or ❌",
            fields=[
                ["Description", current.description],
                ["Subject", current.subject, True],
                ["At", current.date.strftime("%A %B %d, %Y (%m/%d/%y) at %I:%M %p"), True]
            ]
        )
        message = await context.send(embed=embed)
        react = await get_reacts(context, self.client, message, ["✅", "❌"])
        if react.emoji == "✅":
            await context.send("Successfully added exam!")
        elif react.emoji == "❌":
            await context.send("Cancelled adding exam!")
        else:
            raise Exception("You've broken Python!")

    #New User
    @commands.command(name='profile', brief="Set up your profile", description="Set up your profile to start planning out your School Life")
    async def newuser(self, context):
        embed=create_embed(
            "Time to add a new user",
            description="To add a new user, we will need the person's name and school ID number. Please enter your full name."
        )
        message = await context.send(embed=embed)
        resp = await self.client.wait_for("message", check=check(context.author, context.channel))
        current = User()
        goodName = False
        while(goodName==False):
            if ' ' in resp.content:
                current.firstName = resp.content.split(' ')[0]
                current.lastName = resp.content.split(' ')[1]
                current.fullName = current.firstName + current.lastName
                goodName = True
            elif ',' in resp.content:
                current.firstName = resp.content.split(',')[0]
                current.lastName = resp.content.split(',')[1]
                current.fullName = current.firstName + current.lastName
                goodName = True
            else:
                await context.send("Invalid name! Please enter your full name")
                goodName = False
        embed=create_embed(
            f"Continue your Profile, {current.firstName}",
            description="Please enter your school student ID! This is so that you can be recognized by your teachers or students."
        )
        message = await context.send(embed=embed)
        resp = await self.client.wait_for("message", check=check(context.author, context.channel))
        current.schoolID = resp.content
        embed = create_embed(
            f"Confirm your information, {current.firstName}",
            description="Is this correct? ✅ or ❌",
            fields=[
                ["First Name:", current.firstName, True],
                ["Last Name", current.lastName, True],
                ["School ID", current.schoolID]
            ]
        )
        message = await context.send(embed=embed)
        react = await get_reacts(context, self.client, message, ["✅", "❌"])
        if react.emoji == "✅":
            await context.send("Successfully set your profile!")
        elif react.emoji == "❌":
            await context.send("Cancelled your profile!")
        else:
            raise Exception("You've broken Python!")
          


def setup(client):
    client.add_cog(Setup(client))