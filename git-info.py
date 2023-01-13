import git
import datetime

def git_status(git_dir):
    repo = git.Repo(git_dir)
    active_branch = repo.active_branch.name
    local_changes = repo.is_dirty()
    head_commit = repo.head.commit
    recent_commit = (datetime.datetime.now().replace(tzinfo=None) - head_commit.authored_datetime.replace(tzinfo=None)).days < 7
    blame_rufus = head_commit.author.name == "Rufus"
    
    print("active branch:", active_branch)
    print("local changes:", local_changes)
    print("recent commit:", recent_commit)
    print("blame Rufus:", blame_rufus)

#git_status("C:/Users/kjash/Desktop/Imp/Syracuse University/Semester 3/Mobile Application Prog/Transact-iOS-Mobile-Application")
git_status("path/to/your/local/git/repo")
