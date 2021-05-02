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
            Class("Biology Honors", "Bio Honors Period 4! Room 68, Second Floor. Have fun learning Biology!", [ None, "8-9","9-10","10-11", "11-12",None, "7-8"], "Mr. Jeff"),
            Task("Homework Three", "Biology Honors", "Read Pages 23-31 in your textbook and take notes", datetime(2021, 5, 5)),
            Class("Pre-Calculus", "Pre-Calc Period 1! Room 45a, First Floor. Math is cool!", ["9-10","10-11","11-12",None,"7-8",None,"8-9"], "Ms. Russo"),
            Task("Assignment Three", "Pre-Calculus", "Finish the problems on quadratic equations.", datetime(2021, 5, 6)),
            Class("American History", "History Period 2, Room 21, First Floor.", ["10-11","11-12",None,"7-8","8-9",None,"9-10"], "Mr. Singer"),
            Task("Essay One", "American History","Finish your essays on the importance of the Madison v. Marbury case", datetime(2021, 5, 7)),
            Exam("History Quiz One", "American History", "Short quiz on the importance of Washington's presidential precident", datetime(2021, 5, 6, 8, 00)),
            Class("English Honors", "Honors English Period 3, at Room 33, First Floor. Please come prepared with notebooks, pencils, and your books.", ["11-12", "12-1", "7-8","8-9","9-10","12-1","10-11"], "Mrs. Berg"),
            Task("Essay One","English Honors", "Please submit your rough drafts of your essay on the importance of Beowulf in Old English literature", datetime(2021, 5, 10)),
            Class("Biology Honors", "Bio Honors Period 4! Room 68, Second Floor. Have fun learning Biology!",[ None, "8-9","9-10","10-11", "11-12",None, "7-8"], "Mr. Jeff")
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
                ["Date/Time", "\n\n".join(str(n.at[(current_day + 1) % 7]) if isinstance(n.at, list) else str(n.at) for n in next10), True],
                ["Teacher/Class", "\n\n".join(n.subject for n in next10), True],
                ["Key", "🏫 Class, 📚 Task, 📝 Exam"]
            ]
        )
        await context.send(embed=embed)
    @commands.command(name = "tasks", aliases = ['view tasks','View Tasks'], 
    brief = "View your upcoming tasks", description = "View your next ten tasks!")
    async def viewTasks(self, context):
      #index = 0
      #while(index<10):
        #next10[i]=results[i]
        next10 = [
            Task("Homework Three", "Biology Honors", "Read Pages 23-31 in your textbook and take notes", datetime(2021, 5, 5)),
            Task("Assignment Three", "Pre-Calculus", "Finish the problems on quadratic equations.", datetime(2021, 5, 6)),
            Task("Essay One","English Honors", "Please submit your rough drafts of your essay on the importance of Beowulf in Old English literature", datetime(2021, 5, 10)),
            Task("Extra Credit", "Biology Honors", "Watch the Discovery Channel and take notes", datetime(2021, 5, 11)),
            Task("Homework Four", "Biology Honors", "Read Pages 34-45 in your textbook and take notes", datetime(2021, 5, 11)),
            Task("Assignment Four", "Pre-Calculus", "Finish the problems on quadratic equations.", datetime(2021, 5, 12)),
            Task("Reading Five", "American History", "Read the fifth chapter in your textbooks", datetime(2021, 5, 13)),
            Task("Reading Six", "American History", "Read the fifth chapter in your textbooks", datetime(2021, 5, 20)),
            Task("Homework Five", "Biology Honors", "Read Pages 48-60 in your textbook and take notes", datetime(2021, 5, 17)),
            Task("Assignment Five", "Pre-Calculus", "Finish the problems on logarithmic equations.", datetime(2021, 5, 18)),
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
                ["Key", "🏫 Class, 📚 Task, 📝 Exam"]
            ]
            )
        await context.send(embed=embed)
    @commands.command(name = "exams", aliases = ['View Exams'], 
    brief = "View your upcoming tasks", description = "View your next ten exams!")
    async def viewExams(self, context):
        next10 = [
            Exam("History Quiz One", "American History", "Short     quiz on the importance of Washington's presidential precident", datetime(2021, 5, 6, 8, 00)),
            Exam("English Quiz One", "English Honors", "Quiz on Beowulf.", datetime(2021, 5, 7, 10, 00)),
            Exam("Bio Quiz One", "Biology Honors", "Will cover the parts of the cell, open notes", datetime(2021, 5, 10, 9, 00)),
            Exam("Calc Quiz One", "Pre-Calculus", "Quiz on      quadratic equations, bring your calculator!", datetime(2021, 5, 12, 11, 00)),
            Exam("Bio Quiz Two", "Biology Honors", "Short quiz on recent reading assignment", datetime(2021, 5, 17, 9, 00)),
            Exam("Calc Quiz Two", "Pre-Calculus", "Quiz on logarithms and logarithmic equations.", datetime(2021, 5, 19, 11, 00)),
            Exam("History Quiz Two", "American History", "Short assessment of your understanding of the early presidents",datetime(2021, 5, 20, 8, 00)),
            Exam("Bio Test One", "Biology Honors", "Short quiz on recent reading assignment", datetime(2021, 5, 31, 9, 00)),
            Exam("Calc Test One", "Pre-Calculus", "Covers the material learned this semester", datetime(2021, 6, 2, 11,00)),
            Exam("History Test One", "American History", "Covers the material thus far assigned", datetime(2021, 6, 3, 8, 00))
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
                ["Key", "🏫 Class, 📚 Task, 📝 Exam"]
            ]
        )
        await context.send(embed=embed)
    



def setup(client):
    client.add_cog(Current(client))