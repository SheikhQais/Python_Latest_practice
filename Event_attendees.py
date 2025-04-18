invited = {'Ali', 'Zara', 'Ahmed', 'Noor', 'Usman'}
attended = {'Ahmed', 'Noor', 'Usman', 'Sara'}

invited_and_attended = invited.intersection(attended)
print("These are all who were invited and attended:",invited_and_attended)

attended_not_invited = attended.difference(invited)
print("These are those who attended but not invited:",attended_not_invited)

invited_not_attended = invited.difference(invited_and_attended)
print("These are, who were invited but not attended",invited_not_attended)

invited.add("Hassan")
print("This is updated invites:",invited)