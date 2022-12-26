import Head from 'next/head';
import Transactions from './Transactions';


export default function Home() {
  return (
    <>
      <Head>
        <title>Transactions System</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <Transactions />
    </>
  )
}
