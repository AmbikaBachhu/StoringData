import gspread
gc = gspread.service_account(filename='test.json')
sh = gc.open_by_key('1g2daLwurjj6XihtsRtmSgM5FGm0i3o8fDSjxdTAAW80')
worksheet = sh.sheet1
user = ["Shiva","shiva@gmail.com","9898989898"]
worksheet.append_row(user)
