import axios from 'axios';

const API_URL = `${window.location.origin}/suggestions`;

export function getSuggestions(prefix) {
  if (!prefix.length) return [];
  return new Promise(async (resolve, _reject) => {
    try {
      const { data } = await axios.post(API_URL, { prefix });
      resolve(data.map((word) => {
        return word.substring(prefix.length, word.length);
      }));
    } catch(e) {
      resolve([]);
    }
  })
}

export function removeNonAlpha(text) {
  return text.toLowerCase().replace(/[^0-9abcçdefgğhıijklmnoöprsştuüvyz]/gi, '');
}
