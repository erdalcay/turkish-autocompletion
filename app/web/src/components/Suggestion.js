import '../styles/Suggestion.css';

export default function Suggestion({prefix, suffix}) {
  return (
    <div className="suggestion">
      <p>{prefix}<strong>{suffix}</strong></p>
    </div>
  );
}