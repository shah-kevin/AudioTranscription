from typing import Dict, List, Any
import faster_whisper

class EndpointHandler():
    def __init__(self, path=""):
        self.model = faster_whisper.WhisperModel('ivrit-ai/faster-whisper-v2-d3-e3', device='cuda')

    def __call__(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
       data args:
            inputs (:obj: `str`)
            date (:obj: `str`)
      Return:
            A :obj:`list` | `dict`: will be serialized and returned
        """
        # get inputs
        #inputs = data.pop("inputs",data)
        #date = data.pop("date", None)

        # check if date exists and if it is a holiday
        #if date is not None and date in self.holidays:
        #  return [{"label": "happy", "score": 1}]


        # run normal prediction
        #prediction = self.pipeline(inputs)
        return {'text' : 'bender is great!'}
 
