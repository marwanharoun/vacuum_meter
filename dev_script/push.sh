
echo Enter commit description:
read DESC

git status
git add . #(or specific file instead of .)
git status
git commit -m "$DESC"
git status
git push
