story = '''Today I went to the zoo. I saw a(n) ___________ (adjective)
_____________(Noun) jumping up and down in its tree.
He _____________(verb, past tense) __________(adverb)
through the large tunnel that led to its _______(adjective)
__________(noun). '''


print('Welcome to madlingo. Lets get started!')

adj1 = str(input('Enter an adjective: '))
noun1 = str(input('Enter a noun: '))
verb1 = str(input('Enter a verb (past tense): '))
adverb1 = str(input('Enter an adverb: '))
adj2 = str(input('Enter an adjective: '))
noun2 = str(input('Enter a noun: '))

libs = [adj1, noun1, verb1, adverb1, adj2, noun2]

story = 'Today I went to the zoo. I saw a(n) ' + libs[0] + '\ ' + libs[1] + ' jumping up and down in its tree. He ' + libs[2] + '\ ' + libs[3] + ' through the large tunnel that led  to its ' + libs[4] + '\ ' + libs[5] + '.'

print(story)