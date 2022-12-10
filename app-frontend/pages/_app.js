import 'tailwindcss/tailwind.css'
import TransactionState from '../context/transactions/TransactionState';

function MyApp({ Component, pageProps }) {
  return (
    <TransactionState>
      <Component {...pageProps} />
    </TransactionState>
  )
}

export default MyApp