import axios from 'axios';

export const resetCount = async ( camera_name: String) => {
  try {
    const response = await axios.get(`/${camera_name}/reset`);
    return response.data;
  } catch (error) {
    console.error('Error publishing data:', error);
    throw error;
  }
};