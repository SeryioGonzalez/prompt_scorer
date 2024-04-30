

def score_prompt(input_prompt, llm_client, model, rule_file='rules.txt', temperature=0):

   # Read the rules file
   evaluation_rules = open("rules.txt", "r").read()
   delimiter = "####"

   system_message = f"""
   You are an AI expert in prompt engineering best practices. 
   Your task is to help optimize input prompts presented to you following certain rules later described.
   ########### RULES ###########
   ########### END OF RULES ###########
   {evaluation_rules}
   ########### EVALUATION PROCESS ###########
   You will evaluate an input prompt across the following steps provided and assess the quality of the input prompt based on the specific guielines

   ########### INPUT PROMPT FORMAT ###########
   The input prompt will be delimited with four hashtags, i.e. {delimiter}. 

   ########### EXPECTED OUTPUT FORMAT ###########
   Use the following output format, structured in columns. Do not include a blank line after each rule evaluation:
   RULE EVALUATIONS: 
   Rule 01 - <OK_OR_KO> - <Rule 1 evaluation>
      - <IF RULE NOT OK AND THE ISSUE IS IN A SPECIFIC LOCATION OF THE INPUT PROMPT, QUOTE THE SPECIFIC CHUNK OF THE INPUT PROMPT WHERE YOU SEE THE ISSUE. IF THE ISSUE IS IN THE WHOLE INPUT PROMPT. DO NOT QUOTE IT>
   .....
   Rule N - <OK_OR_KO_OR_NA> - <Rule N evaluation>

   RESULT SUMMARY: 
   <Number_of_rules_OK> out of <Total_number_of_rules> rules passed
   <Number_of_rules_KO> out of <Total_number_of_rules> rules not applicable
   <Number_of_rules_KO> out of <Total_number_of_rules> rules not OK
   """

   messages =  [  
      {'role':'system', 'content': system_message},    
      {'role':'user',   'content': f"{delimiter}{input_prompt}{delimiter}"},  
   ] 
   response = llm_client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
   response_content = response.choices[0].message.content

   print(response_content)

