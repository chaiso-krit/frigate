import axios from 'axios';

export const resetCount = async ( camera_name: string) => {
  const confirmed = window.confirm(`Are you sure you want to reset the camera ${camera_name}?`);
  if (confirmed) {
    try {
      const response = await axios.get(`/${camera_name}/reset`);
      alert(`${camera_name} has been reset`);
      return response.data;
    } catch (error) {
      console.error('Error resetting camera ${camera_name}:', error);
      alert(`Error resetting camera ${camera_name} failed.`);
      throw error;
    }
  }
  else {
    alert('Camera reset canceled.');
    return null;
  }
};