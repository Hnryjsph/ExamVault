from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Collection, CustomUser
from django.db.models import Q

# View for the questions
@login_required
def questions(request):
	user = CustomUser(id = request.user.id)
	collections = user.collection_set.all()


	questions = Question.objects.all()

	context = {
		"questions": questions,
		"collections": collections
	}
	return render(request,"questions.html", context)

# View for the details when a question is clicked
@login_required
def details(request, id):
	question = get_object_or_404(Question, id = id)
	context = {
		'question': question,
	}
	return render(request, "details.html", context)

# View that returns all the collections
@login_required
def collections(request):
	user = CustomUser(id = request.user.id)
	collections = user.collection_set.all()
	context = {"collections": collections}
	return render(request, 'collections.html', context)


# View that is routed to, to remove a collection
@login_required
def collection_remove(request, id):
	user = CustomUser(id = request.user.id)
	collections = user.collection_set.all()
	context = {'collections': collections}
	if request.method == "GET":
		
		collection = Collection.objects.get(id=id)
		collection.delete()
		collections = user.collection_set.all()
		context = {'collections': collections}
		return render(request, 'collections.html', context)
    
	return render(request, 'collections.html', context)

# A view that is routed to, to remove a question
# from a collection
@login_required
def question_remove(request, id):
	user = CustomUser(id = request.user.id)
	collections = user.collection_set.all()
	context = {'collections': collections}
	if request.method == "GET":
		
		question = Question.objects.get(id=id)
		collection = Collection.objects.filter(questions__id=id)[0]
		collection.questions.remove(question)
		collections = user.collection_set.all()
		context = {'collections': collections}
		return render(request, 'collections.html', context)
    
	return render(request, 'collections.html', context)


# View that implements the serach functionality 
@login_required
def search(request):
	context = {"questions": []}
	if request.method == "GET":
		q = request.GET['query']
		subject = Q(subject__icontains=q)
		title = Q(title__icontains = q)
		content = Q(content_form_text__icontains = q)
		questions = Question.objects.filter(subject|title|content)

		context = {'questions':questions}

		return render(request, 'search.html', context)

	return render(request, 'search.html', context)

# A view that adds a question to a collection that exists or new
@login_required
def bookmark(request, id):
	user = CustomUser(id = request.user.id)
	collections = user.collection_set.all()

	if request.method == "POST":
	
		if request.POST['collection'] != "Existing collections":
		
			collection_id = int(request.POST['collection'])
			
			collection = get_object_or_404(Collection, id = collection_id)
			prev_list = collection.questions.all()
			
			question = Question.objects.get(id = id)
			collection.questions.add(question)
			collection.save()
			return redirect('/questions/collections/')
		elif request.POST['collection_name']:
			
			title = request.POST['collection_name']
			user = request.user
			question = Question.objects.get(id = id)
			collection = Collection()
			collection.title = title
			collection.user = user 
			collection.save()
			collection.questions.add(question)
			

			return redirect('/questions/collections/')

	context = {"collections": collections}
	return render(request, 'bookmark.html', context)