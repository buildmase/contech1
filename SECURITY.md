# Security Notes

## API Key Storage

Your OpenAI API key is stored in:
- `backend/.env` - Local development (NOT committed to git)

## Important Security Rules

1. ✅ **NEVER commit `.env` files to git** - They're in `.gitignore`
2. ✅ **Never share your API key publicly**
3. ✅ **Rotate keys if exposed** - Go to OpenAI dashboard to regenerate
4. ✅ **Use environment variables in production** - Don't hardcode keys

## For Production Deployment

When deploying to Vercel/Railway/etc:
1. Set `OPENAI_API_KEY` as an environment variable in the platform
2. Don't upload `.env` files
3. The backend will read from environment variables automatically

## If Key is Compromised

1. Go to https://platform.openai.com/api-keys
2. Delete the compromised key
3. Create a new key
4. Update `.env` file locally
5. Update production environment variables

## Current Setup

- ✅ `.env` file created in `backend/` directory
- ✅ `.gitignore` configured to exclude `.env` files
- ✅ Backend loads key from `.env` automatically
- ✅ Key is never hardcoded in source code

