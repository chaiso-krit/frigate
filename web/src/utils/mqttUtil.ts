import axios from 'axios';

export const resetCount = async ( camera_name: String) => {
  const confirmed = window.confirm(`Are you sure you want to reset the camera ${camera_name}?`);
  if (confirmed) {
    try {
      const response = await axios.get(`/${camera_name}/reset`);
      alert(`${camera_name} has been reset`); // แก้ไขคำว่า "reseted" เป็น "reset"
      return response.data;
    } catch (error) {
      console.error('Error publishing data:', error);
      alert(`Error resetting ${camera_name} failed.`);
      throw error;
    }
  }
  else {
    alert('Camera reset canceled.');
    return null;
  }
};