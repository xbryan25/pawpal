import useCookies from 'cookie-universal'
import { isTokenValid } from '@/utils/isTokenValid'

export function useAuthToken() {
  const cookies = useCookies()
  const token = cookies.get('access_token')
  const valid = isTokenValid(token)
  return { token, valid }
}