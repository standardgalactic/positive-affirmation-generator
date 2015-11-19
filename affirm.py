
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

# http://www.secasa.com.au/pages/101-phrases-of-praise/
# http://www.creativeaffirmations.com/anxiety.html
# http://www.creativeaffirmations.com/daily-affirmations.html
# http://www.creativeaffirmations.com/stress-management-affirmations.html

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
    "Super job",
    
    
    
    "Take a time-out. Practice yoga, listen to music, meditate, get a massage, or learn relaxation techniques. Stepping back from the problem helps clear your head.",
    "Eat well-balanced meals. Do not skip any meals. Do keep healthful, energy-boosting snacks on hand.",
    "Limit alcohol and caffeine, which can aggravate anxiety and trigger panic attacks.",
    "Get enough sleep. When stressed, your body needs additional sleep and rest.",
    "Exercise daily to help you feel good and maintain your health.",
    "Take deep breaths. Inhale and exhale slowly.",
    "Count to 10 slowly. Repeat, and count to 20 if necessary.",
    "Do your best. Instead of aiming for perfection, which isn't possible, be proud of however close you get.",
    "Accept that you cannot control everything. Put your stress in perspective: Is it really as bad as you think?",
    "Welcome humor. A good laugh goes a long way.",
    "Maintain a positive attitude. Make an effort to replace negative thoughts with positive ones.",
    "Get involved. Volunteer or find another way to be active in your community, which creates a support network and gives you a break from everyday stress.",
    "Learn what triggers your anxiety. Is it work, family, school, or something else you can identify? Write in a journal when you're feeling stressed or anxious, and look for a pattern.",
    "Talk to someone. Tell friends and family you're feeling overwhelmed, and let them know how they can help you. Talk to a physician or therapist for professional help.",
    "Get help online. Lantern ( https://golantern.com/anxiety/?utm_source=adaa ) offers online programs guided by professional coaches to help you turn healthy anxiety management into a habit. (Sponsored)",

    "5 X 30: Jog, walk, bike, or dance three to five times a week for 30 minutes.",
    "Set small daily goals and aim for daily consistency rather than perfect workouts. It's better to walk every day for 15-20 minutes than to wait until the weekend for a three-hour fitness marathon. Lots of scientific data suggests that frequency is most important.",  
    "Find forms of exercise that are fun or enjoyable. Extroverted people often like classes and group activities. People who are more introverted often prefer solo pursuits.",
    "Distract yourself with an iPod or other portable media player to download audiobooks, podcasts, or music. Many people find it's more fun to exercise while listening to something they enjoy.",
    "Recruit an \"exercise buddy.\" It's often easier to stick to your exercise routine when you have to stay committed to a friend, partner, or colleague.",
    "Be patient when you start a new exercise program. Most sedentary people require about four to eight weeks to feel coordinated and sufficiently in shape so that exercise feels easier.",


    "I release any anxiety I am holding onto.",
    "My current state of being is peaceful.",
    "I am calm.",
    "Each and every day, my circumstances are improving.",
    "Peace. Peace. Peace...",
    "I embrace Divine balance in my life. Everything is as it should be.",
    "I am consciously aware of the calm silence of my spirit.",
    "My awareness is anchored in tranquility.",
    "I am in the Divine flow of life.",
    "I am stable during life's ups and downs.", 
    "I am willing to let my anxious thoughts go. Each day I embrace a laid-back attitude.",
    "I choose to breathe deeply.",
    "From head to toe, I am relaxed.",
    "I am centered.",

    "Today, I will act out of love.",
    "I choose to graciously extend kindness to everyone I meet.",
    "I will do my absolute best.",
    "I will make choices that demonstrate the care I have for my body.",
    "I freely express gratitude for the many blessings I receive.",
    "I will speak kindly to and of others.",
    "I choose to see the good in the people I interact with today.",
    "I will set aside time to be silent and breath.",
    "I have the power to control my reactions to the challenges I will face.",
    "I choose to see each obstacle as an opportunity to grow.",

    "Breathe in; breathe out. Breathe in; breathe out. Breathe in; breathe out.",
    "I choose to focus on the things I can control.",
    "I place my attention on the next thing to do, and only the next thing to do.",
    "I release the things that are not my responsibility to control.",
    "I allow myself to take a break and do something I enjoy.",
    "I am willing to delegate a portion of my responsibilities.",
    "I am okay. All will be okay.",
    "I choose to approach my problems with a calm heart and mind.",
    "Things will be what they will be. I cannot change the past or completely control the future.",
    "I relax into the present moment knowing that this is the only thing that needs my attention right now."

    "Each day I take a small step toward achieving my goals.",
    "I am willing to step outside of my comfort zone to accomplish the goals I set for myself.",
    "The path toward my goal is clear.",
    "I am willing to devote time and energy toward my goals. They are a priority in my life.",
    "I honor my mission and values by pursuing my goals.",
    "I can clearly see my goal already accomplished. ",
    "I accept that there will be challenges when pursuing my goals. I have the knowledge and ability to overcome anything in my path.",
    "The resources I need are becoming available to help me achieve my goals. ",
    "My hard work is paying off already.",
    "I only focus on the next step to take and trust that I am being lead toward the best and highest fulfillment of my goals.",
    "Today is filled with opportunity. Everywhere I look I see it, and I trust my intuition to follow where it leads. ",
    "Good Morning Life! I am so grateful to be alive today.",
    "Today I will trust divine guidance to head my actions knowing that I will be brought to joy & prosperity.",
    "Good Morning! Yes, it will be a good morning and a good day!",
    "I am grateful for today.",
    "The sun is shining through my window and through my heart.",
    "I enter this day with an attitude of appreciation.",
    "Today my world is changing for the better. I open my awareness to my shifting reality.",
    "I allow my intuition to guide my actions to day with trust that I am guided toward my highest good.",
    "Today I will be pleasantly surprised.",
    "I enter today with an open mind and a calm presence.",
    "I am proud of myself.",
    "Positive energy flows through me; each cell of my being is awake and alive with joy.",
    "I radiate love and joy to all I meet.",
    "I am whole, complete and perfect just as I am, right where I am at. ",
    "I am more than capable of bringing my dreams to life. ",
    "I love me.",
    "I choose to be on my side. All of my thoughts are pointed toward my positive intentions.",
    "I release all negativity that is blocking the divine expression of who I am. ",
    "I am okay. I am breathing. I am alive. I am experiencing this moment. I release all worry, all thoughts of past and future. I am here, now.",
    "I am safe. There is Divine protection surrounding me.",
]

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
