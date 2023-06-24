from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Collection, CustomUser


@login_required
def questions(request):
	user = CustomUser(id = request.user.id)
	collections = user.collection_set.all()

	if request.method == "POST":
		print(request.POST)
		if request.POST['collection'] != "Existing collections":
			print("Wooooo")
			print(request.POST)
			collection_id = int(request.POST['collection'])

			collection = get_object_or_404(Collection, id = collection_id)
			prev_list = collection.questions.all()
			print(prev_list)
			question = Question.objects.get(id = int(request.POST['question'][0]))
			collection.questions.add(question)
			collection.save()
		elif request.POST['collection_name']:
			
			title = request.POST['collection_name']
			user = request.user
			question = Question.objects.get(id = int(request.POST['question'][0]))
			collection = Collection()
			collection.title = title
			collection.user = user 
			collection.save()
			collection.questions.add(question)
			

			#return redirect('/questions/')


	questions = Question.objects.all()[:10]

	context = {
		"questions": questions,
		"collections": collections
	}
	return render(request,"questions.html", context)


@login_required
def details(request, id):
	question = get_object_or_404(Question, id = id)
	context = {
		'question': question,
	}
	return render(request, "details.html", context)


@login_required
def collections(request):
	user = CustomUser(id = request.user.id)
	collections = user.collection_set.all()
	context = {"collections": collections}
	return render(request, 'collections.html', context)


@login_required
def collection_details(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    context = {'collection': collection}
    return render(request, 'details.html', context)
