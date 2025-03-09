import axios from 'axios';

export const publishData = async ( path: string, data: string) => {
  try {
    const response = await axios.post(path, data);
    return response.data;
  } catch (error) {
    console.error('Error publishing data:', error);
    throw error;
  }
};