"""
Requirements:
  .replit:
    + ignoredPackages = ["your", "pacakges", "here"]
"""

import os

class Install(object):
  def __init__(self, installs = None) -> None:
    if installs:
      print("Installer: Installing Additional Packages...")
      pkg = ' '.join(installs)
      os.system(f"pip install {pkg}")
      
  def help():
    print("""
    Basic -----------------------------
      import basicsetup
      try:
        import my_package
        import another_one
      except:
        Install([
          "my_package",
          "another_one"
        ])
    For Github Repo Installing---------
      import basicsetup
      Install([
        "git+https://github.com/AWeirdScratcher/dishook.git" # git+my-repo-url.git
      ])
    """)
    
async def checkWebhook(channel, name: str, client_id: int):
  w = await channel.webhooks()
  for wk in w:
    if w.name == name and w.user.id == client_id:
      return w.url
  newWebhook = await channel.create_webhook(name=name)
  return newWebhook.url

... # Ellipsis
