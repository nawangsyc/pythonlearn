# 老邢在使用Git过程中的一些记录
## 一.语法篇
### 1. 开始使用前需要登录，共2条命令
 *  git config --global user.name " ";登记用户名   
 *  git config --global user.email " ";登记用户邮箱   
 *  同样，这两条命令也可以用来修改用户名和邮箱地址
### 2. 创建库，共3条命令
 * cd d:/study/git;用来跳转到创建位置   
 * mkdir learngit;在当前路径下创建相应名称的库   
 * pwd;用来查看是否成功创建   
### 3. 初始化文件库，共1条命令
 *	git init   
### 4. 文件的添加与提交，共2条命令
 * git add readme.txt;将要录入的文件添加到后备队列   
 * git commit -m"what you done";提交并为此次提交贴一个标签说明做了说明改动   
### 5. 当前文件及历史版本的查看，共4条命令
 * git status:用来查看当前文件是否存在改动以及需要提交   
 * git diff;用来查看当前文件与上一个版本间的差异   
 * git log;用来查阅所有的历史版本   
 * git log --pretty=oneline;每个版本用一行显示   
 - **warning** 在使用第4句时，注意‘=’两边不要留空格，要连打，如果有空格会报错   
### 6. 版本的回退与前进，
  * git reset --hard HEAD^;退回到上一个版本中，若要退回到前n个版本中，HEAD~n   
  * git reset --hard 6d5703eaa; 前进到指定版本，需要知道相应版本号的前一部分（不能过少）   
  * git reflog;用来查看所有的历史版本，之后可通过相应的版本号进行重置   
### 7. 撤销修改，共2条命令
  * git checkout -- fileName;将工作区中的修改丢弃   
  * git reset HEAD fileName；将暂存区中的内容回退到工作区当中   
### 8. 删除文件，共2条命令
  * git rm fileName;用来删除本地文件   
  * git commit -m"";将删除操作提交到版本库；   
  - **注意** 如果你在这个时候是误删的，那么在第2步用git checkout -- filename 来丢弃修改  
  *			相当于用版本库里的版本替换工作区的版本   
### 9. 远程仓库建立、推送及克隆到本地，共3条命令
  * git remote add origin git@server-name:path/repository-name.git;用来关联远程仓库  
  * git push -u origin master;用来将本地库中的最新内容推送到远端仓库；
  - **注意** 只有第一次向远程仓库推送的时候需要加上‘-u’，之后使用git push origin master即可。  
  * git clone git@github.com:userName/repository-name.git;将远程仓库中的文件克隆到本地仓库。  
### 10. 分支创建及相关操作，共9条命令
  * git branch;查看当前分支   
  * git branch <branchName>；创建给定名称的分支，但不会跳转到给定分支   
  * git checkout <branchName>；切换到指定分支   
  * git checkout -b <branchName>；创建并切换到指定的分支   
  * git merge <branchName>；将指定的分支合并到当前分支   
  * git branch -d <branchName>；删除指定的分支   
  * git log --graph;用来显示各个版本修改过程的分支图，但这是很乱，可以进行一下命令   
    *	git log --graph --pretty=oneline;这样输出的每一个提交版本占用一行，但版本号很长   
    *	git log --graph --pretty=oneline --abbrev-commit;这时版本号只显示一部分   
  * git merge --no-ff -m"note" dev;关闭快速合并，意味着在合并位置是新创建的一个位置，   
    *	而不是向fast merge中一样将新旧位置合成一个   
  * git stash,将当前工作现场保存起来，以便后续恢复，该功能可用于快速现场保存   
    *		git stash list;用来查询现场列表   
    *		git stash pop;恢复之前的现场，并把stash中的相应信删除   
    *		git stash apply;该命令可用来恢复之前的工作现场，但不会从stash中删除相应信息，   
    *	    需要用 git stash drop 来删除对应的信息。   
### 11. 多人协作时的远程仓库操作，共4条命令
 *	git push origin branchName;将本地的分支推送到远程仓库；   
 *	git pull;将远程仓库中的内容抓取到本地，若本地和远程有冲突的时候需要先抓取，解决冲突之后在推送   
 *	git branch --set-upstream branchName origin/branchName;用来设置本地分支与远程仓库中的分支链接   
 *	git remote;用来查询远程仓库   
 *	git remote -v;详细查询远程仓库信息  
 *  git克隆远程仓库指定分支 git clone -b 分支名 仓库地址  
### 12. 标签管理，共8条命令
 * git tag <name>;创建一个HEAD  
 * git tag <name> <要打标签的版本号>;给指定的版本打上指定名称的标签  
 * git tag -a <tagName> -m "\*\*\*"  <指定版本号>;打上标签并写入注释信息  
 * git tag;查看所有已有标签  
 * git show <tagName>;用来显示指定版本号相关信息  
 * git push origin <tagName>;推送一个本地标签  
 * git push origin --tags;推送本地所有未推送过的标签  
 * git tag -d <tagName>;删除一个本地标签  
 * git push origin :refs/tags/<tagName>;删除一个远程标签  
### 13. 修改某次的 commit ,共5步  
  * git rebase <版本号> --interactive; 切换到要修改的commit上  
  * 修改相应的文件  
  * git add <文件>; 添加修改后的文件  
  * git commit --amend; 追加改动到当前 commit 中  
  * git rebase --continue; 回到最新的 commit 上   
### 14. 当前文件合并到指定的 commit ,共  
  * git stash; 暂存当前工作区  
  * git rebase <版本号> --interactive; 切换到要修改的commit上  
  * git stash pop; 恢复最新工作区  
  * git add <文件>; 添加修改后的文件  
  * git commit --amend; 追加改动到当前 commit 中  
  * git rebase --continue; 回到最新的 commit 上  
### 15. 快去切换到上一级目录  
  * @details  
  * 1.cd ..  
### 16. git 添加ignore文件  
  * 参考网址： http://blog.csdn.net/weixin_36401046/article/details/52954408  
  * 打开git后输入 `touch .gitignore`,这时会生成.gitignore文件，在这个文件中写如不需要提交的文件    
### 17. vim [filename]修改文件  
  * 参考网址：https://blog.csdn.net/zshlclzsh/article/details/50434404  
  * 修改完成后，按ESC之后输入":wq"，将会保存并退出,注意冒号  
  * 修改后，输入":w",将会只进行保存而不退出  
  * 修改后，输入":q!",将会直接退出而不保存  
### 18. 查看当前用户名和用户邮箱  
  * git config user.name  
  * git config user.email  
### 19. 将当前提交合并到前面的提交  
  * 参考网址：https://www.cnblogs.com/icepeach/p/5283479.html
  https://stackoverflow.com/questions/33911379/git-rebase-fatal-needed-a-single-revision-invalid-upstream-i
  * git rebase -i --root  
  * git rebase --abort #放弃当前rebase  
  * git rebase --skip #重新开始rebase并跳过现在所进行的处理.  
### 20. git修改gitignore之后生效,共三步：  
  * git rm -r --cached . #清除缓存，不会对文件进行操作，不用担心  
  * git add . #重新trace文件  
  * git commit -m "" #提交和注释  
### 21. git fetch和git pull区别  
### 22. 从指定分支中提取文件到当前分支
  * git checkout 分支名 文件名
### 23. 克隆远程仓库分支
  * git clone -b 分支名 仓库地址
### 24. clone是出现unable to access error 403
  * 在从公司仓库第一次克隆时输错密码，之后在clone时出现了上述问题，解决方法时：重新设置用户名和密码  
  * 命令 `git clone http://userName:password@连接` 之后会弹出之前的用户名和密码更正之后就可以正常克隆了。
  * 在网上还看到了另一种方法，就是禁用ssl安全检测，命令：`git config --system http.sslverify false` 但是由于这个问题出现在同事的电脑上，所以这一方法的可行性没有进行实际验证
### 25. 推送本地分支到远程分支
  * git push origin dev:dev
  * 语法: git push <远程主机名> <本地分支名>:<远程分支名>
### 26. 查看跟踪的文件
  * git ls-files
### 27. 将本地分支推送到远程仓库(创建远程分支)
  * `git checkout -b develop` 首先要在本地创建分支
  * `git push origin develop` 将本地分支推送到远程，远程就会有新的分支了，推送的时候git会提示你，“ * [new branch] develop -> develop”
  * `git branch -r` 完成所有操作之后可以查看远程的分支状态
