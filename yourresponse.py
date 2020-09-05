score = 0
response1 = input( "Which date will you time travel to for the secret location?\n (A) Jan 4, 1984\n (B) Dec 4, 1984\n (C) Feb 4, 1984\n (D) Jul 4, 1984\n" )


if "B" in response1.upper():
    score -= 5
elif "D" in response1.upper():
    score += 10
elif "A" in response1.upper():
    score += 5
    
response2 = input( "On July 4th, you head to:\n (A) The Grand Canyon\n (B) Washington DC\n (C) The Empire State Building\n (D) The corner coffee shop (with a nagging feeling that there was something special about today)\n" )


if "B" in response2.upper():
    score += 10
elif "D" in response2.upper():
    score -=20


if score == 20: 
    print( "You discovered the secret location! You cracked the cryptic note and found the true meaning behind \"oskza ohupo\"!" )
elif score > 0:
    print( "Whoops! You got a little lost along the way, try decrypting the note again!" )
else: 
    print( "What are you doing having a latte and a scone when you're supposed to be at the secret location?!")