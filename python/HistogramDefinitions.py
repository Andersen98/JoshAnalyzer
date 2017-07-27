import FWCore.ParameterSet.Config as cms
from DisappTrks.StandardAnalysis.utilities import *

muonPlots = cms.PSet(
    inputCollection = cms.vstring("muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonPt"),
            title = cms.string("Muon Transverse Momentum; muon p_{t} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
    )
)

massPlot = cms.PSet(
    inputCollection = cms.vstring("muons", "tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("invMassMuonTrack"),
            title = cms.string("Invariant Mass of Muon and Track; mass [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 150),
            inputVariables = cms.vstring(invMassWithMuon ("muon")),
        ),
    )
)

trackPlots = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trkEta"),
            title = cms.string("Track Eta; {eta}"),
            binsX = cms.untracked.vdouble(100, 0, 2.5),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("trkPhi"),
            title = cms.string("Track Phi; {phi}"),
            binsX = cms.untracked.vdouble(500, 0, 6.5),
            inputVariables = cms.vstring("phi"),
        ),
        cms.PSet (
            name = cms.string("trkfitChi2"),
            title = cms.string("{chi}^2 of Track Fit"),
            binsX = cms.untracked.vdouble(500, 0, 100),
            inputVariables = cms.vstring("chi2"),
        ),
        cms.PSet (
            name = cms.string("trkDXY"),
            title = cms.string("d_{xy} of Track"),
            binsX = cms.untracked.vdouble(500, 0, 100),
            inputVariables = cms.vstring("dxy"),
        ),
        cms.PSet (
            name = cms.string("trackIsoVar"),
            title = cms.string("Track Isolation; [GeV]"),
            binsX = cms.untracked.vdouble(300, 0, 1),
            inputVariables = cms.vstring("trackIsoNoPUDRp3 / pt"),
        ),
        cms.PSet (
            name = cms.string("trkCaloHadDepDR03"),
            title = cms.string("HCal Deposition in Track Direction, Cone dR < 0.3; Energy [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 100),
            inputVariables = cms.vstring("caloHadDRp3"),
        ),
        cms.PSet (
            name = cms.string("trkCaloEMDepDR03"),
            title = cms.string("ECal Deposition in Track Direction, Cone dR < 0.3; Energy [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 100),
            inputVariables = cms.vstring("caloEMDRp3"),
        ),
        cms.PSet (
            name = cms.string("trkCaloDepDR03"),
            title = cms.string("Ecal+HCal Deposition in Track Direction, Cone dR < 0.3; Energy [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 100),
            inputVariables = cms.vstring("caloTotDRp3"),
        ),
    )
)

evtVarPlots = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("caloDepdRCone"),
            title = cms.string("ECal Deposition in Track Direction; Energy [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 100),
            inputVariables = cms.vstring("caloDepTrkCone"),
        ),
        cms.PSet (
            name = cms.string("caloDepdRConeZoom"),
            title = cms.string("ECal Deposition in Track Direction; Energy [GeV]"),
            binsX = cms.untracked.vdouble(500, 0, 1),
            inputVariables = cms.vstring("caloDepTrkCone"),
        ),
    )
)
