from django.shortcuts import render
from .models import Tweet
from .forms import TweetForms
from django.shortcuts import get_object_or_404,redirect
# Create your views here.

def index(request):
    return render(request,'index.html')

# list all tweets 
def tweet_list(request):
    tweets=Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

# creating tweets
def tweet_create(request):
    if request.method=='POST':
        form=TweetForms(request.POST,request.FILES)  # by second arg we can also accept files
        # there are built in method for validation
        if form.is_valid():
            tweet=form.save(commit=False) # Converts the form into a Tweet model object, but does not save it to the database yet . False lets you modify the object (e.g., add user) before saving.
            
            tweet.user=request.user # request by default gets an attribute user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForms() # empty form will be given to user
    return render(request,'tweet_form.html',{'form':form})

# editing tweet forms
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user) # konse models ke andar tweet dekhu - 1st param
    if request.method=='POST':
         form=TweetForms(request.POST,request.FILES,instance=tweet)
         if form.is_valid():
            tweet=form.save(commit=False) # commit = false means that we dont want to put it into db
            tweet.user=request.user # request by default gets an attribute user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForms(instance=tweet)
    return render(request,'tweet_form.html',{'form':form})

def tweet_delete(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_confirm_delete.html',{'tweet':tweet})
