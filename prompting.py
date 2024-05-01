
import google.generativeai as genai
import markdown
from google.api_core import retry

from IPython.display import display, Markdown
def factCheck(text):
  GOOGLE_API_KEY="AIzaSyD0C3DIUm1xgwaBc7CvItyjE6uJmBxGMnI"
  genai.configure(api_key=GOOGLE_API_KEY)

  Instruction="""\Please identify if the given text is fake or legitimate.
  Use below criterias to access
  1. Reputation and Credibility: Research the source's background, reputation, and potential biases. Are they known for accuracy and fact-checking? Do they have a history of publishing false or misleading information?

  2. Accuracy and Evidence : Verify the information presented against other reliable sources. Find a sufficient number of sources claiming the truth. Does the information align with established facts and research? Are claims supported by evidence, such as data, statistics, or expert opinions?

  3. Logic and Reason : Evaluate the logic and reasoning presented. Does the information make sense? Are there any logical fallacies or inconsistencies?

  4. Objectivity and Fairness: Consider if the information is presented objectively or if it appears biased or one-sided. Does it present multiple perspectives, or does it only focus on a specific viewpoint?

  5. Language and Tone: Pay attention to the language and tone used. Is it overly emotional, sensationalized, or inflammatory?  Reputable sources typically use neutral and objective language.

  6.Fact-Checking Websites : Utilize fact-checking websites like Snopes, PolitiFact, or FactCheck.org to verify claims and debunk misinformation.

  Provide evidence for each of these criterias.
  Quantify the legitimacy as a probability between 0 and 1
  """

  model = genai.GenerativeModel('gemini-pro')
  use_sys_inst = False

  model_name = 'gemini-1.5-pro-latest' if use_sys_inst else 'gemini-1.0-pro-latest'

  if use_sys_inst:
    model = genai.GenerativeModel(
        model_name, system_instruction=Instruction)
    convo = model.start_chat()

  else:
    model = genai.GenerativeModel(model_name)
    convo = model.start_chat(
        history=[
            {'role': 'user', 'parts': [Instruction]},
            {'role': 'model', 'parts': ['OK I understand. I will do my best!']}
          ])

  @retry.Retry(initial=30)
  def send_message(message):
    return convo.send_message(message)

  #response = model.generate_content("Give me python code to sort a list")




  response = send_message(text)
  
# Assuming response.text contains Markdown content
  markdown_content = response.text

# Convert Markdown to HTML
  html_content = markdown.markdown(markdown_content)

# Print or display HTML content
  print(html_content)
  return html_content