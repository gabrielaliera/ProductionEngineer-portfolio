#! /usr/bin/env bash
RANDOM_NUMBER=$((RANDOM % 100 + 1))
NAME="TEST $RANDOM_NUMBER"
EMAIL="test@email.com"
CONTENT="TESTING $NAME using curl-test.sh"

#Create timeline post
curl --request POST http://localhost:5000/api/timeline_post -d "name=$NAME&email=$EMAIL&content=$CONTENT"

echo "Submitted Post"

#Retrieve all timeline post
ALL_POST=$(curl --request GET http://localhost:5000/api/timeline_post)

##Check if post was adding 
if [[ $ALL_POST =~ $CONTENT ]]; then
    echo "Timeline post was added successfully"
else 
    echo "Failed to add timeline post"

fi

#Delete timeline post
POST_ID=$(echo "$ALL_POST" | jq -r '.timeline_posts[0].id')


echo "Deleting  $POST_ID..."
# Delete the post by ID
curl --request DELETE http://localhost:5000/api/timeline_post/$POST_ID

#Check if deleted
EXIT_CODE=$?
if [ $EXIT_CODE -eq 0 ] ; then
    echo "Timeline post deleted successfully"
else 
    echo "Failed to delete timeline post"

fi
echo "Test completed."