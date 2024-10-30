// fetch_libre_data.js
import { LibreLinkUpClient } from '@diakem/libre-link-up-api-client';

async function fetchData() {
  try {
    const {read} = LibreLinkUpClient({
      username: 'kevinwesleyrijnders@gmail.com',  // Replace with your username
      password: 'JipIsMijnBae1!',  // Replace with your password
      clientVersion: '4.9.0'      // Replace with the appropriate region code
    });

    const response = await read();  // Replace with the actual method

    // eslint-disable-next-line no-console
    console.log(JSON.stringify(response));
  } catch (error) {
    // eslint-disable-next-line no-console
    console.error("Error fetching data:", error);
    process.exit(1);
  }
}

fetchData();