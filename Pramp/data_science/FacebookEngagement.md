This is a collaborative text editor, use it to communicate with your peer in real-time.

What's useful to share? Stuff like:

- Back-of-the-envelope calculations
- Sample data sets and data flows
- Assumptions about the product/domain/problem
- Pseudo code (or you can switch to an actual coding language)
- Links to files and other resources
- Online profiles

Engagement -> Likes, Comments, Shares with a weighted component. Continuous dependent variable - maximize. 

Data -> anything demographic, device, number of devices you use, number of sessions you have in a day (everytime you open in a day), # of friends, Quality of the content, how that content relates to the information you (if its the same topic you will be more involved), same information of your closest friends (N+1), Group feature -> number of groups you are in, and the activities of these groups, interests. 

model: Decision Tree, Random Forest -> the most important variable and use it and it will tell you how many you used, and the importance of each, take the top 30% of your variables and then run it through a linear regression and the linear regression will have a positive or negative coefficent sign.

RMSE = use this to make sure we have the best random forest, and then the features we will use are just another step to understand the weights of the model. 
LIME (Local interpretable model-agnostic explanations) after we do the predictions we try to locally understand why the prediction happened, and its not general to the whole model its just for assisting with the singular prediciton and which feature had a an importance on the direction of the model. 

We are then able to know if variable x had a positive or negative impact. Whats good with this method is that its individual to each feature, so we can then leverage this on a per user basis.
