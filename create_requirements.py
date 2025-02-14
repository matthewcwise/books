prompt = """you are giving an assignment to a python programmer. Tehir job is to write a python program to turn a project gutenberg .txt file into a latex.

Project requirements:
0) Create a template.tex that they use
1) Input a .txt file from Project Gutenberg
2) Clean up the text and format it correctly
3) Output it as a latex file that is typeset and ready for printing
  Formatting should include correct chapters, table of contents, italics, bolding, etc.
  
  Take these project requirements and write a detailed list of tasks for the programmer to complete. Be sure to include all the steps necessary to complete the project.

To help you understand what needs to be done, here are some excerpts from sample txt files:

From Pride and Prejudice:

*** BEGIN EXCERPT 1 ***:

The Project Gutenberg eBook of Pride and Prejudice
    
This ebook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this ebook or online
at www.gutenberg.org. If you are not located in the United States,
you will have to check the laws of the country where you are located
before using this eBook.

Title: Pride and Prejudice

Author: Jane Austen

Release date: June 1, 1998 [eBook #1342]
                Most recently updated: October 29, 2024

Language: English

Credits: Chuck Greif and the Online Distributed Proofreading Team at http://www.pgdp.net (This file was produced from images available at The Internet Archive)


*** START OF THE PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE ***
                            [Illustration:

                             GEORGE ALLEN
                               PUBLISHER

                        156 CHARING CROSS ROAD
                                LONDON

                             RUSKIN HOUSE
                                   ]

                            [Illustration:

               _Reading Jane’s Letters._      _Chap 34._
                                   ]




                                PRIDE.
                                  and
                               PREJUDICE

                                  by
                             Jane Austen,

                           with a Preface by
                           George Saintsbury
                                  and
                           Illustrations by
                             Hugh Thomson

                         [Illustration: 1894]

                       Ruskin       156. Charing
                       House.        Cross Road.

                                London
                             George Allen.




             CHISWICK PRESS:--CHARLES WHITTINGHAM AND CO.
                  TOOKS COURT, CHANCERY LANE, LONDON.




                            [Illustration:

                          _To J. Comyns Carr
                      in acknowledgment of all I
                       owe to his friendship and
                    advice, these illustrations are
                         gratefully inscribed_

                            _Hugh Thomson_
                                   ]




PREFACE.

[Illustration]


_Walt Whitman has somewhere a fine and just distinction between “loving
by allowance” and “loving with personal love.” This distinction applies
to books as well as to men and women; and in the case of the not very
numerous authors who are the objects of the personal affection, it
brings a curious consequence with it. There is much more difference as
to their best work than in the case of those others who are loved “by
allowance” by convention, and because it is felt to be the right and
proper thing to love them. And in the sect--fairly large and yet
unusually choice--of Austenians or Janites, there would probably be
found partisans of the claim to primacy of almost every one of the
novels. To some the delightful freshness and humour of_ Northanger
Abbey, _its completeness, finish, and_ entrain, _obscure the undoubted
critical facts that its scale is small, and its scheme, after all, that
of burlesque or parody, a kind in which the first rank is reached with
difficulty._ Persuasion, _relatively faint in tone, and not enthralling
in interest, has devotees who exalt above all the others its exquisite
delicacy and keeping. The catastrophe of_ Mansfield Park _is admittedly
theatrical, the hero and heroine are insipid, and the author has almost
wickedly destroyed all romantic interest by expressly admitting that
Edmund only took Fanny because Mary shocked him, and that Fanny might
very likely have taken Crawford if he had been a little more assiduous;
yet the matchless rehearsal-scenes and the characters of Mrs. Norris and
others have secured, I believe, a considerable party for it._ Sense and
Sensibility _has perhaps the fewest out-and-out admirers; but it does
not want them._


*** END EXCERPT 1 ***:

*** BEGIN EXCERPT 2 ***:
[Illustration: List of Illustrations.]


                                                                    PAGE

Frontispiece                                                          iv

Title-page                                                             v

Dedication                                                           vii

Heading to Preface                                                    ix

Heading to List of Illustrations                                     xxv

Heading to Chapter I.                                                  1

“He came down to see the place”                                        2

Mr. and Mrs. Bennet                                                    5

[Illustration: ·PRIDE AND PREJUDICE·




Chapter I.]


It is a truth universally acknowledged, that a single man in possession
of a good fortune must be in want of a wife.

However little known the feelings or views of such a man may be on his
first entering a neighbourhood, this truth is so well fixed in the minds
of the surrounding families, that he is considered as the rightful
property of some one or other of their daughters.

“My dear Mr. Bennet,” said his lady to him one day, “have you heard that
Netherfield Park is let at last?”

Mr. Bennet replied that he had not.

“But it is,” returned she; “for Mrs. Long has just been here, and she
told me all about it.”

Mr. Bennet made no answer.

“Do not you want to know who has taken it?” cried his wife, impatiently.

“_You_ want to tell me, and I have no objection to hearing it.”

[Illustration:

“He came down to see the place”

[_Copyright 1894 by George Allen._]]

This was invitation enough.

“Why, my dear, you must know, Mrs. Long says that Netherfield is taken
by a young man of large fortune from the north of England; that he came
down on Monday in a chaise and four to see the place, and was so much
delighted with it that he agreed with Mr. Morris immediately; that he is
to take possession before Michaelmas, and some of his servants are to be
in the house by the end of next week.”

“What is his name?”

“Bingley.”

“Is he married or single?”

“Oh, single, my dear, to be sure! A single man of large fortune; four or
five thousand a year. What a fine thing for our girls!”

“How so? how can it affect them?”

“My dear Mr. Bennet,” replied his wife, “how can you be so tiresome? You
must know that I am thinking of his marrying one of them.”

“Is that his design in settling here?”

“Design? Nonsense, how can you talk so! But it is very likely that he
_may_ fall in love with one of them, and therefore you must visit him as
soon as he comes.”

“I see no occasion for that. You and the girls may go--or you may send
them by themselves, which perhaps will be still better; for as you are
as handsome as any of them, Mr. Bingley might like you the best of the
party.”

“My dear, you flatter me. I certainly _have_ had my share of beauty, but
I do not pretend to be anything extraordinary now. When a woman has five
grown-up daughters, she ought to give over thinking of her own beauty.”

“In such cases, a woman has not often much beauty to think of.”

“But, my dear, you must indeed go and see Mr. Bingley when he comes into
the neighbourhood.”

“It is more than I engage for, I assure you.”

“But consider your daughters. Only think what an establishment it would
be for one of them. Sir William and Lady Lucas are determined to go,
merely on that account; for in general, you know, they visit no new
comers. Indeed you must go, for it will be impossible for _us_ to visit
him, if you do not.”

“You are over scrupulous, surely. I dare say Mr. Bingley will be very
glad to see you; and I will send a few lines by you to assure him of my
hearty consent to his marrying whichever he chooses of the girls--though
I must throw in a good word for my little Lizzy.”

“I desire you will do no such thing. Lizzy is not a bit better than the
others: and I am sure she is not half so handsome as Jane, nor half so
good-humoured as Lydia. But you are always giving _her_ the preference.”

“They have none of them much to recommend them,” replied he: “they are
all silly and ignorant like other girls; but Lizzy has something more of
quickness than her sisters.”

“Mr. Bennet, how can you abuse your own children in such a way? You take
delight in vexing me. You have no compassion on my poor nerves.”

“You mistake me, my dear. I have a high respect for your nerves. They
are my old friends. I have heard you mention them with consideration
these twenty years at least.”

“Ah, you do not know what I suffer.”

“But I hope you will get over it, and live to see many young men of four
thousand a year come into the neighbourhood.”

“It will be no use to us, if twenty such should come, since you will not
visit them.”

“Depend upon it, my dear, that when there are twenty, I will visit them
all.”

Mr. Bennet was so odd a mixture of quick parts, sarcastic humour,
reserve, and caprice, that the experience of three-and-twenty years had
been insufficient to make his wife understand his character. _Her_ mind
was less difficult to develope. She was a woman of mean understanding,
little information, and uncertain temper. When she was discontented, she
fancied herself nervous. The business of her life was to get her
daughters married: its solace was visiting and news.

[Illustration: M^{r.} & M^{rs.} Bennet

[_Copyright 1894 by George Allen._]]




[Illustration:

“I hope Mr. Bingley will like it”

[_Copyright 1894 by George Allen._]]




CHAPTER II.


[Illustration]

Mr. Bennet was among the earliest of those who waited on Mr. Bingley. He
had always intended to visit him, though to the last always assuring his
wife that he should not go; and till the evening after the visit was
paid she had no knowledge of it. It was then disclosed in the following
manner. Observing his second daughter employed in trimming a hat, he
suddenly addressed her with,--
*** END EXCERPT 2 ***

FROM A CHRISTMAS CAROL:
*** BEGIN EXCERPT 3 ***
The Project Gutenberg eBook of A Christmas Carol in Prose; Being a Ghost Story of Christmas
    
This ebook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this ebook or online
at www.gutenberg.org. If you are not located in the United States,
you will have to check the laws of the country where you are located
before using this eBook.

Title: A Christmas Carol in Prose; Being a Ghost Story of Christmas

Author: Charles Dickens

Illustrator: John Leech

Release date: August 11, 2004 [eBook #46]
                Most recently updated: October 17, 2021

Language: English

Credits: Jose Menendez and David Widger


*** START OF THE PROJECT GUTENBERG EBOOK A CHRISTMAS CAROL IN PROSE; BEING A GHOST STORY OF CHRISTMAS ***




A CHRISTMAS CAROL

IN PROSE
BEING
A Ghost Story of Christmas

by Charles Dickens



PREFACE

I HAVE endeavoured in this Ghostly little book,
to raise the Ghost of an Idea, which shall not put my
readers out of humour with themselves, with each other,
with the season, or with me.  May it haunt their houses
pleasantly, and no one wish to lay it.

Their faithful Friend and Servant,
                                   C. D.
December, 1843.



CONTENTS

Stave   I: Marley's Ghost
Stave  II: The First of the Three Spirits
Stave III: The Second of the Three Spirits
Stave  IV: The Last of the Spirits
Stave   V: The End of It



STAVE I:  MARLEY'S GHOST

MARLEY was dead: to begin with. There is no doubt
whatever about that. The register of his burial was
signed by the clergyman, the clerk, the undertaker,
and the chief mourner. Scrooge signed it: and
Scrooge's name was good upon 'Change, for anything he
chose to put his hand to. Old Marley was as dead as a
door-nail.

Mind! I don't mean to say that I know, of my
own knowledge, what there is particularly dead about
a door-nail. I might have been inclined, myself, to
regard a coffin-nail as the deadest piece of ironmongery
in the trade. But the wisdom of our ancestors
is in the simile; and my unhallowed hands
shall not disturb it, or the Country's done for. You
will therefore permit me to repeat, emphatically, that
Marley was as dead as a door-nail.

Scrooge knew he was dead? Of course he did.
How could it be otherwise? Scrooge and he were
partners for I don't know how many years. Scrooge
was his sole executor, his sole administrator, his sole
assign, his sole residuary legatee, his sole friend, and
sole mourner. And even Scrooge was not so dreadfully
cut up by the sad event, but that he was an excellent
man of business on the very day of the funeral,
and solemnised it with an undoubted bargain.

The mention of Marley's funeral brings me back to
the point I started from. There is no doubt that Marley
was dead. This must be distinctly understood, or
nothing wonderful can come of the story I am going
to relate. If we were not perfectly convinced that
Hamlet's Father died before the play began, there
would be nothing more remarkable in his taking a
stroll at night, in an easterly wind, upon his own ramparts,
than there would be in any other middle-aged
gentleman rashly turning out after dark in a breezy
spot--say Saint Paul's Churchyard for instance--
literally to astonish his son's weak mind.

Scrooge never painted out Old Marley's name.
There it stood, years afterwards, above the warehouse
door: Scrooge and Marley. The firm was known as
Scrooge and Marley. Sometimes people new to the
business called Scrooge Scrooge, and sometimes Marley,
but he answered to both names. It was all the
same to him.

Oh! But he was a tight-fisted hand at the grind-stone,
Scrooge! a squeezing, wrenching, grasping, scraping,
clutching, covetous, old sinner! Hard and sharp as flint,
from which no steel had ever struck out generous fire;
secret, and self-contained, and solitary as an oyster. The
cold within him froze his old features, nipped his pointed
nose, shrivelled his cheek, stiffened his gait; made his
eyes red, his thin lips blue; and spoke out shrewdly in his
grating voice. A frosty rime was on his head, and on his
eyebrows, and his wiry chin. He carried his own low
temperature always about with him; he iced his office in
the dog-days; and didn't thaw it one degree at Christmas.

External heat and cold had little influence on
Scrooge. No warmth could warm, no wintry weather
chill him. No wind that blew was bitterer than he,
no falling snow was more intent upon its purpose, no
pelting rain less open to entreaty. Foul weather didn't
know where to have him. The heaviest rain, and
snow, and hail, and sleet, could boast of the advantage
over him in only one respect. They often "came down"
handsomely, and Scrooge never did.

Nobody ever stopped him in the street to say, with
gladsome looks, "My dear Scrooge, how are you?
When will you come to see me?" No beggars implored
him to bestow a trifle, no children asked him
what it was o'clock, no man or woman ever once in all
his life inquired the way to such and such a place, of
Scrooge. Even the blind men's dogs appeared to
know him; and when they saw him coming on, would
tug their owners into doorways and up courts; and
then would wag their tails as though they said, "No
eye at all is better than an evil eye, dark master!"

*** END EXCERPT 3 ***
*** BEGIN  EXCERPT 4 ***

"Now, I'll tell you what, my friend," said Scrooge, "I
am not going to stand this sort of thing any longer. And
therefore," he continued, leaping from his stool, and giving
Bob such a dig in the waistcoat that he staggered back into
the Tank again; "and therefore I am about to raise your
salary!"

Bob trembled, and got a little nearer to the ruler. He
had a momentary idea of knocking Scrooge down with it,
holding him, and calling to the people in the court for help
and a strait-waistcoat.

"A merry Christmas, Bob!" said Scrooge, with an earnestness
that could not be mistaken, as he clapped him on the
back. "A merrier Christmas, Bob, my good fellow, than I
have given you, for many a year! I'll raise your salary, and
endeavour to assist your struggling family, and we will discuss
your affairs this very afternoon, over a Christmas bowl of
smoking bishop, Bob! Make up the fires, and buy another
coal-scuttle before you dot another i, Bob Cratchit!"


Scrooge was better than his word. He did it all, and
infinitely more; and to Tiny Tim, who did NOT die, he was
a second father. He became as good a friend, as good a
master, and as good a man, as the good old city knew, or
any other good old city, town, or borough, in the good old
world. Some people laughed to see the alteration in him,
but he let them laugh, and little heeded them; for he was
wise enough to know that nothing ever happened on this
globe, for good, at which some people did not have their fill
of laughter in the outset; and knowing that such as these
would be blind anyway, he thought it quite as well that they
should wrinkle up their eyes in grins, as have the malady in
less attractive forms. His own heart laughed: and that was
quite enough for him.

He had no further intercourse with Spirits, but lived upon
the Total Abstinence Principle, ever afterwards; and it was
always said of him, that he knew how to keep Christmas
well, if any man alive possessed the knowledge. May that
be truly said of us, and all of us! And so, as Tiny Tim
observed, God bless Us, Every One!






*** END OF THE PROJECT GUTENBERG EBOOK A CHRISTMAS CAROL IN PROSE; BEING A GHOST STORY OF CHRISTMAS ***


    

Updated editions will replace the previous one—the old editions will
be renamed.

Creating the works from print editions not protected by U.S. copyright
law means that no one owns a United States copyright in these works,
so the Foundation (and you!) can copy and distribute it in the United
States without permission and without paying copyright
royalties. Special rules, set forth in the General Terms of Use part
of this license, apply to copying and distributing Project
Gutenberg™ electronic works to protect the PROJECT GUTENBERG™
concept and trademark. Project Gutenberg is a registered trademark,
and may not be used if you charge for an eBook, except by following
the terms of the trademark license, including paying royalties for use
of the Project Gutenberg trademark. If you do not charge anything for
copies of this eBook, complying with the trademark license is very
easy. You may use this eBook for nearly any purpose such as creation
of derivative works, reports, performances and research. Project
Gutenberg eBooks may be modified and printed and given away—you may
do practically ANYTHING in the United States with eBooks not protected
by U.S. copyright law. Redistribution is subject to the trademark
license, especially commercial redistribution.


START: FULL LICENSE

THE FULL PROJECT GUTENBERG LICENSE

PLEASE READ THIS BEFORE YOU DISTRIBUTE OR USE THIS WORK

To protect the Project Gutenberg™ mission of promoting the free
distribution of electronic works, by using or distributing this work
(or any other work associated in any way with the phrase “Project
Gutenberg”), you agree to comply with all the terms of the Full
Project Gutenberg™ License available with this file or online at
www.gutenberg.org/license.

Section 1. General Terms of Use and Redistributing Project Gutenberg™
electronic works

1.A. By reading or using any part of this Project Gutenberg™
electronic work, you indicate that you have read, understand, agree to
and accept all the terms of this license and intellectual property
(trademark/copyright) agreement. If you do not agree to abide by all
the terms of this agreement, you must cease using and return or
destroy all copies of Project Gutenberg™ electronic works in your
possession. If you paid a fee for obtaining a copy of or access to a
Project Gutenberg™ electronic work and you do not agree to be bound
by the terms of this agreement, you may obtain a refund from the person
or entity to whom you paid the fee as set forth in paragraph 1.E.8.

1.B. “Project Gutenberg” is a registered trademark. It may only be
used on or associated in any way with an electronic work by people who
agree to be bound by the terms of this agreement. There are a few
things that you can do with most Project Gutenberg™ electronic works
even without complying with the full terms of this agreement. See
paragraph 1.C below. There are a lot of things you can do with Project
Gutenberg™ electronic works if you follow the terms of this
agreement and help preserve free future access to Project Gutenberg™
electronic works. See paragraph 1.E below.

1.C. The Project Gutenberg Literary Archive Foundation (“the
Foundation” or PGLAF), owns a compilation copyright in the collection
of Project Gutenberg™ electronic works. Nearly all the individual
works in the collection are in the public domain in the United
States. If an individual work is unprotected by copyright law in the
United States and you are located in the United States, we do not
claim a right to prevent you from copying, distributing, performing,
displaying or creating derivative works based on the work as long as
all references to Project Gutenberg are removed. Of course, we hope
that you will support the Project Gutenberg™ mission of promoting
free access to electronic works by freely sharing Project Gutenberg™
works in compliance with the terms of this agreement for keeping the
Project Gutenberg™ name associated with the work. You can easily
comply with the terms of this agreement by keeping this work in the
same format with its attached full Project Gutenberg™ License when
you share it without charge with others.

1.D. The copyright laws of the place where you are located also govern
what you can do with this work. Copyright laws in most countries are
in a constant state of change. If you are outside the United States,
check the laws of your country in addition to the terms of this
agreement before downloading, copying, displaying, performing,
distributing or creating derivative works based on this work or any
other Project Gutenberg™ work. The Foundation makes no
representations concerning the copyright status of any work in any
country other than the United States.

1.E. Unless you have removed all references to Project Gutenberg:

1.E.1. The following sentence, with active links to, or other
immediate access to, the full Project Gutenberg™ License must appear
prominently whenever any copy of a Project Gutenberg™ work (any work
on which the phrase “Project Gutenberg” appears, or with which the
phrase “Project Gutenberg” is associated) is accessed, displayed,
performed, viewed, copied or distributed:

    This eBook is for the use of anyone anywhere in the United States and most
    other parts of the world at no cost and with almost no restrictions
    whatsoever. You may copy it, give it away or re-use it under the terms
    of the Project Gutenberg License included with this eBook or online
    at www.gutenberg.org. If you
    are not located in the United States, you will have to check the laws
    of the country where you are located before using this eBook.
  
1.E.2. If an individual Project Gutenberg™ electronic work is
derived from texts not protected by U.S. copyright law (does not
contain a notice indicating that it is posted with permission of the
copyright holder), the work can be copied and distributed to anyone in
the United States without paying any fees or charges. If you are
redistributing or providing access to a work with the phrase “Project
Gutenberg” associated with or appearing on the work, you must comply
either with the requirements of paragraphs 1.E.1 through 1.E.7 or
obtain permission for the use of the work and the Project Gutenberg™
trademark as set forth in paragraphs 1.E.8 or 1.E.9.

1.E.3. If an individual Project Gutenberg™ electronic work is posted
with the permission of the copyright holder, your use and distribution
must comply with both paragraphs 1.E.1 through 1.E.7 and any
additional terms imposed by the copyright holder. Additional terms
will be linked to the Project Gutenberg™ License for all works
posted with the permission of the copyright holder found at the
beginning of this work.

1.E.4. Do not unlink or detach or remove the full Project Gutenberg™
License terms from this work, or any files containing a part of this
work or any other work associated with Project Gutenberg™.

1.E.5. Do not copy, display, perform, distribute or redistribute this
electronic work, or any part of this electronic work, without
prominently displaying the sentence set forth in paragraph 1.E.1 with
active links or immediate access to the full terms of the Project
Gutenberg™ License.

1.E.6. You may convert to and distribute this work in any binary,
compressed, marked up, nonproprietary or proprietary form, including
any word processing or hypertext form. However, if you provide access
to or distribute copies of a Project Gutenberg™ work in a format
other than “Plain Vanilla ASCII” or other format used in the official
version posted on the official Project Gutenberg™ website
(www.gutenberg.org), you must, at no additional cost, fee or expense
to the user, provide a copy, a means of exporting a copy, or a means
of obtaining a copy upon request, of the work in its original “Plain
Vanilla ASCII” or other form. Any alternate format must include the
full Project Gutenberg™ License as specified in paragraph 1.E.1.

1.E.7. Do not charge a fee for access to, viewing, displaying,
performing, copying or distributing any Project Gutenberg™ works
unless you comply with paragraph 1.E.8 or 1.E.9.

1.E.8. You may charge a reasonable fee for copies of or providing
access to or distributing Project Gutenberg™ electronic works
provided that:

    • You pay a royalty fee of 20% of the gross profits you derive from
        the use of Project Gutenberg™ works calculated using the method
        you already use to calculate your applicable taxes. The fee is owed
        to the owner of the Project Gutenberg™ trademark, but he has
        agreed to donate royalties under this paragraph to the Project
        Gutenberg Literary Archive Foundation. Royalty payments must be paid
        within 60 days following each date on which you prepare (or are
        legally required to prepare) your periodic tax returns. Royalty
        payments should be clearly marked as such and sent to the Project
        Gutenberg Literary Archive Foundation at the address specified in
        Section 4, “Information about donations to the Project Gutenberg
        Literary Archive Foundation.”
    
    • You provide a full refund of any money paid by a user who notifies
        you in writing (or by e-mail) within 30 days of receipt that s/he
        does not agree to the terms of the full Project Gutenberg™
        License. You must require such a user to return or destroy all
        copies of the works possessed in a physical medium and discontinue
        all use of and all access to other copies of Project Gutenberg™
        works.
    
    • You provide, in accordance with paragraph 1.F.3, a full refund of
        any money paid for a work or a replacement copy, if a defect in the
        electronic work is discovered and reported to you within 90 days of
        receipt of the work.
    
    • You comply with all other terms of this agreement for free
        distribution of Project Gutenberg™ works.
    

1.E.9. If you wish to charge a fee or distribute a Project
Gutenberg™ electronic work or group of works on different terms than
are set forth in this agreement, you must obtain permission in writing
from the Project Gutenberg Literary Archive Foundation, the manager of
the Project Gutenberg™ trademark. Contact the Foundation as set
forth in Section 3 below.

1.F.

1.F.1. Project Gutenberg volunteers and employees expend considerable
effort to identify, do copyright research on, transcribe and proofread
works not protected by U.S. copyright law in creating the Project
Gutenberg™ collection. Despite these efforts, Project Gutenberg™
electronic works, and the medium on which they may be stored, may
contain “Defects,” such as, but not limited to, incomplete, inaccurate
or corrupt data, transcription errors, a copyright or other
intellectual property infringement, a defective or damaged disk or
other medium, a computer virus, or computer codes that damage or
cannot be read by your equipment.

1.F.2. LIMITED WARRANTY, DISCLAIMER OF DAMAGES - Except for the “Right
of Replacement or Refund” described in paragraph 1.F.3, the Project
Gutenberg Literary Archive Foundation, the owner of the Project
Gutenberg™ trademark, and any other party distributing a Project
Gutenberg™ electronic work under this agreement, disclaim all
liability to you for damages, costs and expenses, including legal
fees. YOU AGREE THAT YOU HAVE NO REMEDIES FOR NEGLIGENCE, STRICT
LIABILITY, BREACH OF WARRANTY OR BREACH OF CONTRACT EXCEPT THOSE
PROVIDED IN PARAGRAPH 1.F.3. YOU AGREE THAT THE FOUNDATION, THE
TRADEMARK OWNER, AND ANY DISTRIBUTOR UNDER THIS AGREEMENT WILL NOT BE
LIABLE TO YOU FOR ACTUAL, DIRECT, INDIRECT, CONSEQUENTIAL, PUNITIVE OR
INCIDENTAL DAMAGES EVEN IF YOU GIVE NOTICE OF THE POSSIBILITY OF SUCH
DAMAGE.

1.F.3. LIMITED RIGHT OF REPLACEMENT OR REFUND - If you discover a
defect in this electronic work within 90 days of receiving it, you can
receive a refund of the money (if any) you paid for it by sending a
written explanation to the person you received the work from. If you
received the work on a physical medium, you must return the medium
with your written explanation. The person or entity that provided you
with the defective work may elect to provide a replacement copy in
lieu of a refund. If you received the work electronically, the person
or entity providing it to you may choose to give you a second
opportunity to receive the work electronically in lieu of a refund. If
the second copy is also defective, you may demand a refund in writing
without further opportunities to fix the problem.

1.F.4. Except for the limited right of replacement or refund set forth
in paragraph 1.F.3, this work is provided to you ‘AS-IS’, WITH NO
OTHER WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO WARRANTIES OF MERCHANTABILITY OR FITNESS FOR ANY PURPOSE.

1.F.5. Some states do not allow disclaimers of certain implied
warranties or the exclusion or limitation of certain types of
damages. If any disclaimer or limitation set forth in this agreement
violates the law of the state applicable to this agreement, the
agreement shall be interpreted to make the maximum disclaimer or
limitation permitted by the applicable state law. The invalidity or
unenforceability of any provision of this agreement shall not void the
remaining provisions.

1.F.6. INDEMNITY - You agree to indemnify and hold the Foundation, the
trademark owner, any agent or employee of the Foundation, anyone
providing copies of Project Gutenberg™ electronic works in
accordance with this agreement, and any volunteers associated with the
production, promotion and distribution of Project Gutenberg™
electronic works, harmless from all liability, costs and expenses,
including legal fees, that arise directly or indirectly from any of
the following which you do or cause to occur: (a) distribution of this
or any Project Gutenberg™ work, (b) alteration, modification, or
additions or deletions to any Project Gutenberg™ work, and (c) any
Defect you cause.

Section 2. Information about the Mission of Project Gutenberg™

Project Gutenberg™ is synonymous with the free distribution of
electronic works in formats readable by the widest variety of
computers including obsolete, old, middle-aged and new computers. It
exists because of the efforts of hundreds of volunteers and donations
from people in all walks of life.

Volunteers and financial support to provide volunteers with the
assistance they need are critical to reaching Project Gutenberg™’s
goals and ensuring that the Project Gutenberg™ collection will
remain freely available for generations to come. In 2001, the Project
Gutenberg Literary Archive Foundation was created to provide a secure
and permanent future for Project Gutenberg™ and future
generations. To learn more about the Project Gutenberg Literary
Archive Foundation and how your efforts and donations can help, see
Sections 3 and 4 and the Foundation information page at www.gutenberg.org.

Section 3. Information about the Project Gutenberg Literary Archive Foundation

The Project Gutenberg Literary Archive Foundation is a non-profit
501(c)(3) educational corporation organized under the laws of the
state of Mississippi and granted tax exempt status by the Internal
Revenue Service. The Foundation’s EIN or federal tax identification
number is 64-6221541. Contributions to the Project Gutenberg Literary
Archive Foundation are tax deductible to the full extent permitted by
U.S. federal laws and your state’s laws.

The Foundation’s business office is located at 809 North 1500 West,
Salt Lake City, UT 84116, (801) 596-1887. Email contact links and up
to date contact information can be found at the Foundation’s website
and official page at www.gutenberg.org/contact

Section 4. Information about Donations to the Project Gutenberg
Literary Archive Foundation

Project Gutenberg™ depends upon and cannot survive without widespread
public support and donations to carry out its mission of
increasing the number of public domain and licensed works that can be
freely distributed in machine-readable form accessible by the widest
array of equipment including outdated equipment. Many small donations
($1 to $5,000) are particularly important to maintaining tax exempt
status with the IRS.

The Foundation is committed to complying with the laws regulating
charities and charitable donations in all 50 states of the United
States. Compliance requirements are not uniform and it takes a
considerable effort, much paperwork and many fees to meet and keep up
with these requirements. We do not solicit donations in locations
where we have not received written confirmation of compliance. To SEND
DONATIONS or determine the status of compliance for any particular state
visit www.gutenberg.org/donate.

While we cannot and do not solicit contributions from states where we
have not met the solicitation requirements, we know of no prohibition
against accepting unsolicited donations from donors in such states who
approach us with offers to donate.

International donations are gratefully accepted, but we cannot make
any statements concerning tax treatment of donations received from
outside the United States. U.S. laws alone swamp our small staff.

Please check the Project Gutenberg web pages for current donation
methods and addresses. Donations are accepted in a number of other
ways including checks, online payments and credit card donations. To
donate, please visit: www.gutenberg.org/donate.

Section 5. General Information About Project Gutenberg™ electronic works

Professor Michael S. Hart was the originator of the Project
Gutenberg™ concept of a library of electronic works that could be
freely shared with anyone. For forty years, he produced and
distributed Project Gutenberg™ eBooks with only a loose network of
volunteer support.

Project Gutenberg™ eBooks are often created from several printed
editions, all of which are confirmed as not protected by copyright in
the U.S. unless a copyright notice is included. Thus, we do not
necessarily keep eBooks in compliance with any particular paper
edition.

Most people start at our website which has the main PG search
facility: www.gutenberg.org.

This website includes information about Project Gutenberg™,
including how to make donations to the Project Gutenberg Literary
Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks.

*** END EXCERPT 4***
"""


prompt2 = """
# Instructions for the Programmer

Below is a comprehensive set of instructions for converting a raw Project Gutenberg `.txt` file into a properly formatted LaTeX document, ready for typesetting and printing. These instructions include all steps you need to take, including references to sample text excerpts, metadata extraction, and LaTeX formatting guidelines.

## Project Requirements

**Overall Goal:**  
Write a Python program that:
1. Takes as input a Project Gutenberg `.txt` file.
2. Cleans up and formats the text.
3. Outputs a `.tex` file using a LaTeX template (`template.tex`), resulting in a print-ready, typeset PDF of the book.

**Details:**
- You must create a `template.tex` file that the Python script will use as a base.
- The `.txt` file from Project Gutenberg contains the raw text of a public-domain work (e.g., "Pride and Prejudice" by Jane Austen or "A Christmas Carol" by Charles Dickens).
- The output `.tex` should include proper LaTeX document structure (title page, table of contents, chapters, possible front matter like a preface, etc.).
- Properly format chapters, italics, bolding, and other text features.
- Remove all Project Gutenberg licensing text and extraneous material outside the main text.

## Example Input Text Structure

Project Gutenberg `.txt` files generally have:
- A header section with metadata and disclaimers.
- **Start marker:** `*** START OF THE PROJECT GUTENBERG EBOOK ... ***`
- The main text content after the start marker.
- **End marker:** `*** END OF THE PROJECT GUTENBERG EBOOK ... ***`
- A license section and other trailing text after the end marker.

For example, in "Pride and Prejudice", you might see lines like:

*** START OF THE PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE ***

Title: Pride and Prejudice Author: Jane Austen

[ ... main text ... ]

*** END OF THE PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE ***


For "A Christmas Carol", similarly:
*** START OF THE PROJECT GUTENBERG EBOOK A CHRISTMAS CAROL IN PROSE; BEING A GHOST STORY OF CHRISTMAS ***

Title: A Christmas Carol in Prose; Being a Ghost Story of Christmas Author: Charles Dickens

[ ... main text ... ]

*** END OF THE PROJECT GUTENBERG EBOOK A CHRISTMAS CAROL ... ***

Your script should:
- Identify and strip out everything before `*** START OF THE PROJECT GUTENBERG EBOOK ... ***` and after `*** END OF THE PROJECT GUTENBERG EBOOK ... ***`.
- Extract metadata (Title, Author) from the header area.
- Ignore the Project Gutenberg license text at the end.

## Step-by-Step Instructions

### 1. Prepare the LaTeX Template
Create a `template.tex` with:
- A proper preamble:
  ```latex
  \documentclass[12pt]{book}
  \usepackage[T1]{fontenc}
  \usepackage[utf8]{inputenc}
  \usepackage{lmodern}
  \usepackage{graphicx}
  \usepackage{hyperref}
  \usepackage{csquotes}

  \title{<TITLE_PLACEHOLDER>}
  \author{<AUTHOR_PLACEHOLDER>}
  \date{}

  \begin{document}
  \frontmatter
  \maketitle
  \tableofcontents
  \mainmatter
  % The main text will be inserted here by the Python script
  \end{document}

Ensure this template includes placeholders for the title and author that your script will replace, as well as a place to insert the cleaned text.
### 2. Input Handling
Your Python script will take one .txt file as input (e.g., pride_and_prejudice.txt).
Read the entire file into memory or stream it line by line.
### 3. Strip Project Gutenberg Header and Footer
Identify the start marker: *** START OF THE PROJECT GUTENBERG EBOOK ... ***
Identify the end marker: *** END OF THE PROJECT GUTENBERG EBOOK ... ***
Discard all text before the start marker and after the end marker.
Discard the license text that follows the end marker.
Remove any references to www.gutenberg.org and other non-content text.
### 4. Extract Metadata
From the section just after the start marker, look for lines like:


Title: Pride and Prejudice
Author: Jane Austen
Store the extracted title and author in variables. These will replace <TITLE_PLACEHOLDER> and <AUTHOR_PLACEHOLDER> in the LaTeX template.
If available, also note release date, illustrator, and other metadata. You may include them as front matter (e.g., a preface page) if desired.
### 5. Clean and Normalize the Text
Normalize whitespace:
Remove extra blank lines.
Convert multiple spaces to single spaces.
Convert quotes and dashes to LaTeX-friendly forms:
Use \enquote{...} or ‘‘...’’ for quotes.
Replace — with --- for em-dashes.
Remove any extraneous bracketed notes that do not form part of the main narrative, or format them appropriately. For instance:
[Illustration: ...] lines could be turned into \emph{(Illustration: ... )} or, if you have the illustrations, insert a figure environment. If no images are provided, just italicize the note:

\emph{[Illustration: Reading Jane’s Letters]}
### 6. Identify Chapters and Sections
Most Project Gutenberg texts have clear chapter headers:
Often CHAPTER I, CHAPTER II, etc., or Chapter 1, Chapter 2.
Replace these with \chapter{...} commands. For example:

CHAPTER I
becomes:

\chapter{Chapter I}
If there's a preface or introduction section:
Insert \chapter*{Preface} (unnumbered) before \mainmatter.
Place this text before the \tableofcontents.
For a foreword, introduction, or other front matter, handle similarly as \chapter*{Introduction}.
### 7. Table of Contents and Lists
The \tableofcontents command in template.tex will generate a TOC based on the \chapter commands found in the final .tex file.
If the text has a list of illustrations or other special sections, consider adding \listoffigures if figures are used, or a custom section enumerating illustrations.
### 8. Footnotes and Endnotes
If the text contains footnotes in a recognizable pattern (e.g., (Footnote: ...)), convert them to LaTeX footnotes:

... some text\footnote{This is the content of the footnote.}
### 9. Assembly of the Final .tex File
Your Python script should:
Load template.tex into a string or memory.
Insert the extracted Title and Author into the placeholders.
Process the main text and produce the LaTeX body with proper \chapter commands and formatted text.
Insert this cleaned and structured body into the template at the designated spot (just before \end{document}).
Save the output as output.tex (or another desired filename).
### 10. Compile and Check Output
After generating output.tex, run pdflatex (or xelatex/lualatex if Unicode support is needed) multiple times to produce a PDF.
Check the PDF for formatting issues, correct chapters, and that all extraneous text is removed.
If any problems arise (e.g., missing characters, odd formatting), adjust the cleaning logic and re-run.
### 11. Documentation and Handoff
Include a README.md explaining how the Python script works, the input .txt file it expects, and how to produce the PDF.
The user should be able to run the script with a simple command (e.g., python convert.py input.txt) and then run pdflatex output.tex to get the final PDF.
Notes on Sample Excerpts
Below are some lines from the provided sample excerpts to guide formatting decisions:

Pride and Prejudice:


*** START OF THE PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE ***

Title: Pride and Prejudice
Author: Jane Austen

[Illustration: ...]
PREFACE.

Walt Whitman has somewhere a fine and just ...
You could format the preface as:


\chapter*{Preface}
Walt Whitman has somewhere ...
When encountering a chapter:


Chapter I.
It is a truth universally acknowledged...
This could become:


\chapter{Chapter I}
It is a truth universally acknowledged...
A Christmas Carol:


*** START OF THE PROJECT GUTENBERG EBOOK A CHRISTMAS CAROL IN PROSE; BEING A GHOST STORY OF CHRISTMAS ***

Title: A Christmas Carol in Prose; Being a Ghost Story of Christmas
Author: Charles Dickens

STAVE I: MARLEY'S GHOST

Marley was dead: to begin with...
STAVE I might become:


\chapter{Stave I: Marley's Ghost}
Marley was dead: to begin with...
At the end:


*** END OF THE PROJECT GUTENBERG EBOOK A CHRISTMAS CAROL ...
Everything after this line should be removed.

By following these instructions step-by-step, you will produce a well-structured, print-ready LaTeX document from a raw Project Gutenberg .txt file. The final PDF will contain a properly formatted title page, table of contents, chapters, and any front matter, free of licensing and extraneous text.
"""