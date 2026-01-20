   
91939@ANJALI MINGW64 ~
$ cd ~/interns_ai_ml_assignments

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462|REVERTING)
$ git status
On branch INT2026-1462
Your branch is up to date with 'origin/INT2026-1462'.

You are currently reverting commit fd4c373.
  (all conflicts fixed: run "git revert --continue")
  (use "git revert --skip" to skip this patch)
  (use "git revert --abort" to cancel the revert operation)

nothing to commit, working tree clean

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462|REVERTING)
$ remote set -url origin https://github.com/cepialabs/interns_ai_ml_assignments.git
bash: remote: command not found

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462|REVERTING)
$ git remote set -url origin https://github.com/cepialabs/interns_ai_ml_assignments.git
error: unknown subcommand: `set'
usage: git remote [-v | --verbose]
   or: git remote add [-t <branch>] [-m <master>] [-f] [--tags | --no-tags] [--mirror=<fetch|push>] <name> <url>
   or: git remote rename [--[no-]progress] <old> <new>
   or: git remote remove <name>
   or: git remote set-head <name> (-a | --auto | -d | --delete | <branch>)
   or: git remote [-v | --verbose] show [-n] <name>
   or: git remote prune [-n | --dry-run] <name>
   or: git remote [-v | --verbose] update [-p | --prune] [(<group> | <remote>)...]
   or: git remote set-branches [--add] <name> <branch>...
   or: git remote get-url [--push] [--all] <name>
   or: git remote set-url [--push] <name> <newurl> [<oldurl>]
   or: git remote set-url --add <name> <newurl>
   or: git remote set-url --delete <name> <url>

    -v, --[no-]verbose    be verbose; must be placed before a subcommand


91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462|REVERTING)
$ git remote set-url origin https://github.com/cepialabs/interns_ai_ml_assignments.git

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462|REVERTING)
$ git remote -v
origin  https://github.com/cepialabs/interns_ai_ml_assignments.git (fetch)
origin  https://github.com/cepialabs/interns_ai_ml_assignments.git (push)

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462|REVERTING)
$ git checkout INT2026-1462
Already on 'INT2026-1462'
warning: cancelling a revert in progress
Your branch is up to date with 'origin/INT2026-1462'.

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ git checkout -b INT2026-1462
fatal: a branch named 'INT2026-1462' already exists

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ git fetch origin
remote: Enumerating objects: 111, done.
remote: Counting objects: 100% (106/106), done.
remote: Compressing objects: 100% (74/74), done.
remote: Total 111 (delta 16), reused 69 (delta 8), pack-reused 5 (from 1)
Receiving objects: 100% (111/111), 154.93 KiB | 1.28 MiB/s, done.
Resolving deltas: 100% (16/16), completed with 3 local objects.
From https://github.com/cepialabs/interns_ai_ml_assignments
 + 57d184e...a259cfd INT-2026-7586         -> origin/INT-2026-7586  (forced update)
   6444485..788ab75  INT2026-0011          -> origin/INT2026-0011
   a2fb275..afa401a  INT2026-0794          -> origin/INT2026-0794
   8d6862c..7a9c739  INT2026-0885          -> origin/INT2026-0885
   5a7361a..efdb100  INT2026-1740          -> origin/INT2026-1740
 * [new branch]      INT2026-7285          -> origin/INT2026-7285
   165882d..7fb3c7b  INT2026-9043          -> origin/INT2026-9043
   8380d68..1bdeff3  int2026-2177          -> origin/int2026-2177
   064abff..2553e59  main                  -> origin/main
 * [new branch]      revert-9-INT2026-1467 -> origin/revert-9-INT2026-1467

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ git pull origin INT2026-1462 --rebase
From https://github.com/cepialabs/interns_ai_ml_assignments
 * branch            INT2026-1462 -> FETCH_HEAD
Already up to date.

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ mkdir -p week-1/day-2-assignment

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ mv "/c/Users/91939/week -1/day-2-assignment.ipynb" "week-1/day-2-assignment/"

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ ls week-1/day-2-assignment
day-2-assignment.ipynb

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ git add .
warning: in the working copy of 'week-1/day-2-assignment/day-2-assignment.ipynb', LF will be replaced by CRLF the next time Git touches it

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ git commit -m "Week 1 Day 2 Assignment 1 submission"
[INT2026-1462 74f4236] Week 1 Day 2 Assignment 1 submission
 1 file changed, 522 insertions(+)
 create mode 100644 week-1/day-2-assignment/day-2-assignment.ipynb

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ git push origin INT2026-1462
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 130.79 KiB | 14.53 MiB/s, done.
Total 5 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/cepialabs/interns_ai_ml_assignments.git
   412fdee..74f4236  INT2026-1462 -> INT2026-1462

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ git status
On branch INT2026-1462
Your branch is up to date with 'origin/INT2026-1462'.

nothing to commit, working tree clean

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ git rm -r day-2-assignment
fatal: pathspec 'day-2-assignment' did not match any files

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ git rm -r --cached week^C

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ git rm -r --cached week-1/day-2-assignment
rm 'week-1/day-2-assignment/day-2-assignment.ipynb'

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ git commit -m "Removed day-2-assignment folder"
[INT2026-1462 fa06014] Removed day-2-assignment folder
 1 file changed, 522 deletions(-)
 delete mode 100644 week-1/day-2-assignment/day-2-assignment.ipynb

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ git push origin ^C

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ git push origin INT2026-1462
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 312 bytes | 312.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/cepialabs/interns_ai_ml_assignments.git
   74f4236..fa06014  INT2026-1462 -> INT2026-1462

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ ^C

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ ^C

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ ^C

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ ^C

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ ^C

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ ^C

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ ^C

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$ ^C

91939@ANJALI MINGW64 ~/interns_ai_ml_assignments (INT2026-1462)
$



