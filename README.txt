
# Stock Screener Deployment Instructions

## Step 1: Create a new GitHub repository
- Go to https://github.com and create a new repository (e.g. 'stock-screener').

## Step 2: Upload files
- Upload the following files to the root of your repository:
  - stock_screener_app.py
  - requirements.txt
  - Nifty50_Top.xlsx
  - Nifty200_Top.xlsx
  - Midcap_Top.xlsx
  - Smallcap_Top.xlsx

## Step 3: Deploy on Streamlit Cloud
- Go to https://streamlit.io/cloud and sign in with your GitHub account.
- Click on 'New app'.
- Select your GitHub repo and branch.
- Select the file: stock_screener_app.py
- Click 'Deploy'.

## Step 4: Use the app
- Your app will open in a new tab.
- Use the sidebar to select categories and view top companies.

---

For updates:
- Replace Excel files with updated data.
- Redeploy the app.
