# myapp/views.py
from django.shortcuts import render
import pickle
import numpy as np

popularity_df = pickle.load(open(r'C:\Users\Shivani\Downloads\Book-Recommendation-System-main\Book-Recommendation-System-main\popularity.pkl','rb'))
pt = pickle.load(open(r'C:\Users\Shivani\Downloads\Book-Recommendation-System-main\Book-Recommendation-System-main\pt.pkl','rb'))
books = pickle.load(open(r'C:\Users\Shivani\Downloads\Book-Recommendation-System-main\Book-Recommendation-System-main\books.pkl','rb'))
similarity_score = pickle.load(open(r'C:\Users\Shivani\Downloads\Book-Recommendation-System-main\Book-Recommendation-System-main\similarity_score.pkl','rb'))
book_list = pickle.load(open(r'C:\Users\Shivani\Downloads\Book-Recommendation-System-main\Book-Recommendation-System-main\book_list.pkl','rb'))

def recommend_ui(request):
    return render(request, 'recommend/recommend.html')

def recommend_books(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        
        # Assuming pt is a DataFrame containing book titles
        indi = np.where(pt.index == user_input)[0][0]
        print('\n',indi)
        print('\n')
        
        # Assuming similarity_score is a DataFrame containing similarity scores
        similar_items = sorted(list(enumerate(similarity_score[indi])), key=lambda x: x[1], reverse=True)[1:13]

        data = []
        for i in similar_items:
            item = []
            # Assuming books is a DataFrame containing book details
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data.append(item)
        return render(request, 'recommend/recommend.html', {'data': data})


    else:
        return render(request, 'recommend\recommend.html')
def listt(request):
    context = {
        'name': list(books['Book-Title'][1:201].values)
    }
    return render(request, 'recommend/list.html', context)
