@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_news = get_movies('popular')
    upcoming_news = get_movies('upcoming')
    now_showing_news = get_movies('now_playing')
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title, popular = popular_news, upcoming = upcoming_news, now_showing = now_showing_news )