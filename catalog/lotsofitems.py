from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from database_setup import DATABASE
from database_setup import Category, Base, Item, User

engine = create_engine(URL(**DATABASE))
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create user1
User1 = User(name="goku", email="goku@gmail.com",
             picture='http://bit.ly/1O6P9u4')
session.add(User1)
session.commit()

# Create a category1
Category1 = Category(name="Soccer")
session.add(Category1)
session.commit()

# Menu for item1
Item1 = Item(user_id=1,
             name="British Soccer",
             category=Category1,
             description="Challenger Sports British Soccer Camps is the most \
                          popular soccer camp in the country. Over a thousand \
                          Challenger coaches each year have helped the \
                          company develop one of the most innovative \
                          approaches to coaching youth soccer in the US.")
session.add(Item1)
session.commit()

# menu for item2
Item2 = Item(user_id=1,
             name="American Soccer",
             category=Category1,
             description="The American Soccer League (ASL) is an American\
                         soccer league that began play in August 2014.[1] The \
                         league footprint is initially in the northeastern\
                         United States, with expansion to other areas planned \
                         for the future. ASL players are paid, making it \
                         different from the NPSL or PDL models in which \
                         college-eligible players can compete.")
session.add(Item2)
session.commit()


# Create user2
User2 = User(name="vegeta", email="vegeta@gmail.com",
             picture='http://bit.ly/1IsD0mC')
session.add(User2)
session.commit()

# Create a category2
Category2 = Category(name="Snowboarding")
session.add(Category2)
session.commit()

# Menu for item1
Item3 = Item(user_id=2,
             name="Goggles",
             category=Category2,
             description="Goggles are one of the most important pieces of \
             equipment you can purchase; they are just as important as your \
             jacket and pants. Any skier or snowboarder can tell you that not \
             being able to see ruins a day as fast as poor fitting boots or a \
             bad chili dog. All ski and snowboard goggles will offer some \
             basic protection from wind and cold, but beyond the basics there \
             are some key features to consider: lens type, lens color/tint, \
             interchangeable lenses, frame size and fit.")
session.add(Item3)
session.commit()

# menu for item2
Item4 = Item(user_id=2,
             name="Snowboard",
             category=Category2,
             description="Snowboard is a recreational activity and olympic \
             sport that involves descending a slope that is covered with snow \
             while standing on a snowboard attached to a rider's feet. The \
             development of snowboarding was inspired by skateboarding, \
             sledding, surfing and skiing. It was developed in the United \
             States in the 1960s and became a Winter Olympic Sport in 1998. \
             Its popularity (as measured by equipment sales) peaked in 2007 \
             and has been in a decline since.[1]")
session.add(Item4)
session.commit()

Category3 = Category(name="Swimming")
session.add(Category3)
session.commit()

Category4 = Category(name="Racing")
session.add(Category4)
session.commit()

Category5 = Category(name="Running")
session.add(Category5)
session.commit()

Category6 = Category(name="Jumping")
session.add(Category6)
session.commit()

print "added items!"
