import Head from 'next/head';
import Transactions from './Transactions';


export default function Home() {
  return (
    <>
      <Head>
        <title>Mentimeter Accounting System</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Transactions />
    </>
  )
}
