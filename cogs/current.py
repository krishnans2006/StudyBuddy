from discord.ext import commands
from helpers.funcs import create_embed
from models.classModels import Class, Task, Exam

from datetime import datetime

dashboardcodes = {
    "class": "🏫",
    "task": "📚",
    "exam": "📝"
}

c_daysList = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

class Current(commands.Cog, name="current", description="View your current tasks, schedule, exams, and dashboard!"):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name="dashboard", aliases=["db"], brief="View your dashboard", description="View your upcoming classes, tasks, and exams!")
    async def dashboard(self, context):
        next10 = [
            Class("Biology Honors", "Bio Honors Period 4! Room 68, Second Floor. Have fun learning Biology!", [ "7-8", "8-9","9-10","10-11", "11-12",None, None], "Mr. Jeff"),
            Task("Homework Three", "Biology Honors", "Read Pages 23-31 in your textbook and take notes", datetime.now()),
            Class("Pre-Calculus", "Pre-Calc Period 1! Room 45a, First Floor. Math is cool!", ["9-10","10-11","11-12",None,"8-9",None,None], "Ms. Russo"),
            Task("Assignment Three", "Pre-Calculus", "Finish the problems on quadratic equations.", datetime.now()),
            Class("American History", "History Period 2, Room 21, First Floor.", ["10-11","11-12",None,"8-9","9-10",None,None], "Mr. Singer"),
            Task("Essay One", "American History","Finish your essays on the importance of the Madison v. Marbury case", datetime.now()),
            Exam("History Quiz One", "American History", "Short quiz on the importance of Washington's presidential precident", datetime.now()),
            Class("English Honors", "Honors English Period 3, at Room 33, First Floor. Please come prepared with notebooks, pencils, and your books.", ["11-12", None, "8-9","9-10","10-11",None,None], "Mrs. Berg"),
            Task("Essay One","English Honors", "Please submit your rough drafts of your essay on the importance of Beowulf in Old English literature", datetime.now()),
            Class("Biology Honors", "Bio Honors Period 4! Room 68, Second Floor. Have fun learning Biology!",[ "7-8", "8-9","9-10","10-11", "11-12",None, None], "Mr. Jeff")
        ]  
        current_day = int(datetime.now().strftime("%w"))
        embed = create_embed(
            "Your Next 10 Classes, Exams, and Tasks",
            fields=[
                [
                    "Name", 
                    "\n\n".join(
                        [str(dashboardcodes[type(n).__name__.lower()] + " " + n.name) for n in next10]
                    ),
                    True
                ],
                ["Date/Time", "\n\n".join(n.at[current_day] if isinstance(n.at, list) else str(n.at) for n in next10), True],
                ["Teacher/Class", "\n\n".join(n.subject for n in next10), True],
            ],
            footer="Key: 🏫 Class, 📚 Task, 📝 Exam"
        )
        await context.send(embed=embed)
    @commands.command(name = "tasks", aliases = ['view tasks','View Tasks'], 
    brief = "View your upcoming tasks", description = "View your next ten tasks!")
    async def viewTasks(self, context):
        next10 = [
            Task("Homework Three", "Biology Honors", "Read Pages 23-31 in your textbook and take notes", datetime.now()),
            Task("Assignment Three", "Pre-Calculus", "Finish the problems on quadratic equations.", datetime.now()),
            Task("Essay One", "American History","Finish your essays on the importance of the Madison v. Marbury case", datetime.now()),
            Task("Essay One","English Honors", "Please submit your rough drafts of your essay on the importance of Beowulf in Old English literature", datetime.now()),
            Task("Homework Four", "Biology Honors", "Read Pages 34-45 in your textbook and take notes", datetime.now()),
            Task("Assignment Four", "Pre-Calculus", "Finish the problems on quadratic equations.", datetime.now()),
            Task("Reading Five", "American History", "Read the fifth chapter in your textbooks", datetime.now()),
            Task("Reading Four","English Honors","Read the first story of The Canterbury Tales",datetime.now()),
            Task("Homework Five", "Biology Honors", "Read Pages 48-60 in your textbook and take notes", datetime.now()),
            Task("Assignment Five", "Pre-Calculus", "Finish the problems on logarithmic equations.", datetime.now()),
        ]
        current_day = int(datetime.now().strftime("%w"))
        embed = create_embed(
            "Your Next 10 Classes, Exams, and Tasks",
            fields=[
                [
                    "Name", 
                    "\n\n".join(
                        [str(dashboardcodes[type(n).__name__.lower()] + " " + n.name) for n in next10]
                    ),
                    True
                ],
                ["Date/Time", "\n\n".join(n.at[current_day] if isinstance(n.at, list) else str(n.at) for n in next10), True],
                ["Teacher/Class", "\n\n".join(n.subject for n in next10), True],
            ],
            footer="Key: 🏫 Class, 📚 Task, 📝 Exam"
            )
        await context.send(embed=embed)
    @commands.command(name = "exams", aliases = ['View Exams'], 
    brief = "View your upcoming tasks", description = "View your next ten exams!")
    async def viewExams(self, context):
        next10 = [
            Exam("History Quiz One", "American History", "Short               quiz on the importance of Washington's presidential               precident", datetime.now()),
            Exam("Calc Quiz One", "Pre-Calculus", "Quiz on      quadratic equations, bring your calculator!", datetime.now()),
            Exam("English Quiz One", "English Honors", "Quiz on Beowulf.", datetime.now()),
            Exam("Bio Quiz One", "Biology Honors", "Will cover the parts of the cell, open notes", datetime.now()),
            Exam("Calc Quiz Two", "Pre-Calculus", "Quiz on logarithms and logarithmic equations.", datetime.now()),
            Exam("English Essay One", "English Honors", "In class essay on the development of Middle English", datetime.now()),
            Exam("History Quiz Two", "American History", "Short assessment of your understanding of the early presidents", datetime.now()),
            Exam("Bio Quiz Two", "Biology Honors", "Short quiz on recent reading assignment", datetime.now()),
            Exam("History Test One", "American History", "Covers the material thus far assigned", datetime.now()),
            Exam("Calc Test One", "Pre-Calculus", "Covers the material learned this semester", datetime.now())
        ]
        current_day = int(datetime.now().strftime("%w"))
        embed = create_embed(
            fields=[
                [
                    "Name", 
                    "\n\n".join(
                        [str(dashboardcodes[type(n).__name__.lower()] + " " + n.name) for n in next10]
                    ),
                    True
                    ],
                ["Date/Time", "\n\n".join(n.at[current_day] if isinstance(n.at, list) else str(n.at) for n in next10), True],
                ["Teacher/Class", "\n\n".join(n.subject for n in next10), True],
            ],
            footer="Key: 🏫 Class, 📚 Task, 📝 Exam"
        )
        await context.send(embed=embed)
    



def setup(client):
    client.add_cog(Current(client))