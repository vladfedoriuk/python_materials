- to create an empty repo and push to a remote one:
```buildoutcfg
echo "# blog_app" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/vladfedoriuk/blog_app.git
git push -u origin main
```
- or push an existing repository from the command line:
```buildoutcfg
git remote add origin https://github.com/vladfedoriuk/blog_app.git
git branch -M main
git push -u origin main
```