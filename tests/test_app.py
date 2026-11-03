import sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import app

class LeadFlowTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.db=Path(self.tmp.name)/'test.db'
        app.init_db(self.db)
    def tearDown(self): self.tmp.cleanup()
    def test_full_lead_lifecycle(self):
        i=app.create_lead(app.SAMPLES[0],self.db)
        lead=app.get_lead(i,self.db)
        self.assertEqual(lead['stage'],'New')
        analysis=app.demo_analysis(lead)
        self.assertEqual(analysis['priority'],'Hot')
        self.assertEqual(analysis['analysis_mode'],'Demo rules (not AI)')
        app.save_analysis(i,analysis,self.db)
        app.update_lead(i,{'approved':1},self.db)
        self.assertEqual(app.get_lead(i,self.db)['approved'],1)
        app.update_lead(i,{'draft_body':'Edited message'},self.db)
        self.assertEqual(app.get_lead(i,self.db)['approved'],0)
        app.update_lead(i,{'stage':'Meeting booked'},self.db)
        self.assertEqual(app.get_lead(i,self.db)['stage'],'Meeting booked')
    def test_scoring(self):
        scores=[app.demo_analysis(x) for x in app.SAMPLES]
        self.assertGreater(scores[0]['score'],scores[2]['score'])
        self.assertEqual(scores[2]['priority'],'Cold')
    def test_validation(self):
        with self.assertRaises(ValueError): app.create_lead({'name':'','company':'X','need':'Y'},self.db)
        with self.assertRaises(ValueError): app.update_lead(1,{'stage':'Imaginary'},self.db)

if __name__=='__main__': unittest.main()
