#!/home/ubuntu/
cd semi-live/keyword/keyword
#git reset --hard origin/211_features_test
#git pull origin 211_features_test
#cd demo/
docker stop app
echo "y" |docker system prune -a
docker build -t app .
docker run -d -p 5000:5000 --name app app
