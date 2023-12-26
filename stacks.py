# Stacks are LIFO - Last in First out

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

# Remove the last item in the Stack with .pop
last = browsing_session.pop()
print(last)
print(browsing_session)

print(browsing_session[-1]) # -1 Index is for the LAST item in the stack
print("redirected to session:", browsing_session[-1])

if not browsing_session:
    print("disabled")