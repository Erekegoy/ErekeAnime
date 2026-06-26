from core.project_manager import ProjectManager

pm = ProjectManager()

file = pm.create("demo_project")

pm.update_status(file,"finished")

pm.set_video(
    file,
    "outputs/videos/final_video.mp4"
)

print(file)
