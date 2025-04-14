// function startRecognition() 
// {
//     const recognition = new webkitSpeechRecognition();
//     recognition.lang = 'en-IN';
//     recognition.interimResults = false;
//     recognition.maxAlternatives = 1;
  
//     document.getElementById("status").innerText = "Listening...";
  
//     recognition.start();
  
//     recognition.onresult = function(event) 
//     {
//       const speechResult = event.results[0][0].transcript;
//       document.getElementById("status").innerText = `You said: ${speechResult}`;
  
//       fetch('/process', 
//         {
//         method: 'POST',
//         headers: {'Content-Type': 'application/json'},
//         body: JSON.stringify({query: speechResult})
//       })
//       .then(res => res.json())
//       .then(data => {
//         document.getElementById("response").innerText = data.response;
//       });
//     };
  
//     recognition.onerror = function(err) {
//       console.error("Speech error:", err);
//     };
//   }
  




// function startRecognition() {
//     const recognition = new webkitSpeechRecognition();
//     recognition.lang = 'en-IN';
//     recognition.interimResults = false;
//     recognition.continuous = false;
  
//     document.getElementById("status").innerText = "🎙️ Listening...";
  
//     recognition.start();
  
//     recognition.onresult = function(event) {
//       const speechResult = event.results[0][0].transcript;
//       document.getElementById("status").innerText = `You said: "${speechResult}"`;
  
//       fetch('/process', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ query: speechResult })
//       })
//       .then(res => res.json())
//       .then(data => {
//         document.getElementById("response").innerText = data.response;
//         if (data.followUp) {
//           setTimeout(() => {
//             startRecognition();
//           }, 3000);
//         }
//       });
//     };
  
//     recognition.onerror = function() {
//       document.getElementById("status").innerText = "❌ Error occurred. Try again.";
//     };
//   }
  



  
function startRecognition() {
    const recognition = new webkitSpeechRecognition();
    recognition.lang = 'en-IN';
    recognition.interimResults = false;
    recognition.continuous = false;
  
    document.getElementById("status").innerText = "🎙️ Listening...";
  
    recognition.start();
  
    recognition.onresult = function(event) {
      const speechResult = event.results[0][0].transcript;
      document.getElementById("status").innerText = `You said: "${speechResult}"`;
  
      fetch('/process', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: speechResult })
      })
      .then(res => res.json())
      .then(data => {
        document.getElementById("response").innerText = data.response;
        if (data.followUp) {
          setTimeout(() => {
            startRecognition();
          }, 3000);
        }
      });
    };
  
    recognition.onerror = function() {
      document.getElementById("status").innerText = "Error occurred. Try again.";
    };
  }
  