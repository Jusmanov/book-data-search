import pandas as pd

# Scanning and oragnizing the books dataset (books.csv)
df = pd.read_csv('books.csv', delimiter=',')

# Search book function: Takes user input for a title, searches for titles containing user title. Prints results.
def searchBook():
	titleEntry = input("Entry: ").lower()
	df['title'] = df['title'].str.lower()
	book_search_results = df[df['title'].str.contains(titleEntry, case = False, regex = False)]
	print(book_search_results)
def booksByAuthor():
	authorEntry = input("Author name: ")
	df['authors'] = df['authors'].str.lower()
	filtered_df = df[df['authors'].str.contains(authorEntry, case=False, regex=False)]
	if not filtered_df.empty:
		print(f"Books written by author '{authorEntry}':")
		print(filtered_df)
	else:
		print(f"No rows contain the author's name '{authorEntry}'.")
def findRating():
	bookRateEntry = input("Book title: ").lower()
	df['title'] = df['title'].str.lower()
	foundBook = (df[(df['title'] == bookRateEntry)]).index.tolist()
	print(foundBook)
	print(df.loc[foundBook[0], 'title'], "-", df.loc[foundBook[0], 'average_rating'])
def highestRated():
	avgRatings = df.sort_values(by='average_rating', ascending = False)
	return avgRatings
