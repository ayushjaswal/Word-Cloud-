import wordcloud
from matplotlib import pyplot as plt


def upload():
    text_file = open("Word.txt", 'r')
    data = text_file.read()
    text_file.close()
    return data


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we", "our",
                           "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its","they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from",
                           "here", "when", "where", "how", "all", "any", "both", "each", "few", "more", "some", "such",
                           "no", "nor", "too", "very","can", "will", "just"]

    # LEARNER CODE START HERE
    word_lst = file_contents.lower().split()  # splits the string into a list
    new_wrd_lst = []  # empty list that will contain only interesting words
    for word in word_lst:  # iterate through our word list
        if word not in uninteresting_words and word not in punctuations and word.isalpha() == True:  # checks if word has uninteresting word in it
            new_wrd_lst.append(word)  # if not then appends the word to our empty list
    frequencies = {}  # an empty dictionary
    for word in new_wrd_lst:  # iterating through the list
        count = 0
        for wrd in new_wrd_lst:  # nested loop for comparison
            if word == wrd:  # comparing if the word is same
                count += 1  # counting the number of time the word came
        frequencies[word] = count
    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


# Display your wordcloud image

myimage = calculate_frequencies(upload())
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
