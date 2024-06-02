import logo from './logo.svg';
import './App.css';
// import { quiz } from './quiz';
import { quiz } from './election_questions';
import Quiz from 'react-quiz-component';

function App() {
  return (
    <div className="App">
      <Quiz quiz={quiz} shuffle={true} shuffleAnswer={true}/>
    </div>
  );
}

export default App;
