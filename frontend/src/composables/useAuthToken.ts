import useCookies from 'cookie-universal'

export function useAuthToken() {
  const cookies = useCookies()
  const token = cookies.get('access_token')
  return { token }
}