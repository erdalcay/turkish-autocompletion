import { useState, useRef } from 'react';
import Suggestion from './Suggestion';
import { removeNonAlpha, getSuggestions } from '../lib/helpers';
import '../styles/SearchBox.css';

export default function SearchBox() {
  const [inputText, setInputText] = useState('');
  const [displaySuggestions, setDisplaySuggestions] = useState(false);
  const [suggestions, setSuggestions] = useState({});
  const inputElement = useRef(null);

  const handleChange = async ({ target: { value: input }}) => {
    setInputText(input);
    /**
     * Get the last word only & clean up such that
     * only Turkish alphabet characters are retained.
     */
    const words = input.split(' ');
    const prefix = removeNonAlpha(words[words.length - 1]);
    if (!prefix.length) return setDisplaySuggestions(false); 

    const suggestedWords = await getSuggestions(prefix);
    if (!suggestedWords.length) return setDisplaySuggestions(false);

    if (!displaySuggestions) setDisplaySuggestions(true);
    /**
     * @TODO -------- Add ability to select any of the suggested words.
     */
    return setSuggestions({ prefix, suggestedWords });
  }

  const refocus = (inputElement) => {
    inputElement.focus();
  }

  return (
    <section className='search-box-container'>
      <div className='headline'>
        <p>Start typing to get auto-completion</p>
      </div>
      <div className='search-box'>
        <div className='input'>
          <div className='left-padding' />
          <input 
            name='search-input' 
            id='searchInput' 
            spellCheck='false'
            value={inputText}
            autoFocus
            onInput={ handleChange }
            ref={
              element => {
                inputElement.current = element;
              }
            }
          />
          <span 
            className='clear' 
            onClick={() => {
              setInputText(''); setDisplaySuggestions(false); refocus(inputElement.current);
            }}
          >X</span>
        </div>
        <div 
          className={
            'suggestions' +  (displaySuggestions ? ' display' : ' no-display')
          }
          id='suggestions'>
          {
            suggestions.suggestedWords?.length > 0 && 
            suggestions.suggestedWords.map((suggestion, id) => {
              return (
                <Suggestion key={id} prefix={suggestions.prefix} suffix={suggestion}/>
              );
            })
          }
        </div>
      </div>
    </section>
  );
}