
import random

# TODO: return affirmations containing a category tagged somehow


# I don't like doing the extra function for a simple check,
# but it's multi-step so oh well.

import argparse
parser = argparse.ArgumentParser(description="Give me some affirmations.")

# I must use nargs ? to make optional positional arguments, (could also use *)
parser.add_argument('qty',
        metavar="#",
        type=int,
        nargs='?',
        help='number of affirmations to output',
        default=1)

parser.add_argument('-f', '--search',
        type=str,
        nargs='?',
        help='string contained in affirmation',
        default=None)

args = parser.parse_args()

def substr_found(haystack):
    if (haystack.lower().find(args.search) < 0):
        return False
    else:
        return True

affirmations = ["I love you",
    "You're great",
    "Great job",
    "Outstanding",
    "Wonderful",
    "Thanks for helping",
    "I'm so proud of you",
    "Lean on me",
    "You can do it",
    "Terrific",
    "Thanks so much",
    "Perfect",
    "You're super",
    "That's a great idea",
    "Way to go",
    "Great smile",
    "You're the best Good for you",
    "Fabulous",
    "You make me happy",
    "Excellent",
    "You're delightful",
    "You're an inspiration",
    "Thanks for sharing",
    "You did it",
    "Great",
    "You look good",
    "Super work",
    "You're getting there",
    "You're special",
    "Marvelous",
    "You're getting better",
    "You deserve a star",
    "I trust you",
    "Fantastic",
    "You've improved",
    "Very good",
    "You're an angel You're a big help",
    "I'm impressed",
    "You're fun",
    "You're very responsible",
    "Exceptional",
    "Thanks for caring",
    "You're a real pal",
    "You're a super listener You're considerate",
    "Dynamite",
    "You're a joy to be around",
    "Nice work",
    "Hurray for you",
    "You're tops",
    "You're a gem",
    "I listen to you",
    "You're on your way",
    "You're a champ",
    "You'll get it",
    "You've made progress",
    "Beautiful",
    "Keep up the good work",
    "You're so creative",
    "Great imagination",
    "You're very brave",
    "You're special",
    "You've got what it takes",
    "How thoughtful",
    "Good sport",
    "You're #1",
    "How original",
    "Sounds great",
    "How clever",
    "You're on the mark",
    "You're a real friend",
    "Keep trying",
    "I support you",
    "You're the greatest",
    "Much better",
    "Thanks for being honest",
    "I've got faith in you",
    "Well done",
    "Great idea",
    "How artistic",
    "Very nice of you",
    "Great try",
    "What careful work",
    "I like you",
    "You've got it now",
    "Exceptional",
    "That's neat",
    "Wonderful imagination",
    "You're right",
    "You've got heart",
    "You're so smart",
    "You're sweet",
    "Delightful idea What a great kid",
    "Great answer",
    "You deserve a kiss",
    "You're such a smart kid",
    "You brighten my day",
    "Super job"]

if (args.search != None):
    affirmations = filter(substr_found, affirmations)



if (affirmations != []):
    idx = 0
    print ""
    while (idx < args.qty):
        print random.choice(affirmations)
        idx += 1
    print ""
else:
    print "Woops! No matches found."



# TODO: write some tests for practice
