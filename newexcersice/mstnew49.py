# 49. Resume Scanner 


from resume_parser import resumeparse
data = resumeparse.read_file("resume.docx" )
for i in data:
    print(i)
    # for i, j in data.items():
    #     print(f"{i}:>>{j}")

# resume= 
# scan_resume(resume)

