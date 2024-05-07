import os
import argparse
from mido import MidiFile, MidiTrack, Message

path = os.path.realpath(os.path.dirname(__file__))

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Combine two MIDI files.')
parser.add_argument('midi1', type=str, help='Path to the first MIDI file')
parser.add_argument('midi2', type=str, help='Path to the second MIDI file')
parser.add_argument('-o', '--outfile', help='specify output file (default: ./combined.mid)', default=os.path.join(path, 'combined.mid'))
args = parser.parse_args()

# Load the MIDI files
midi1 = MidiFile(args.midi1)
midi2 = MidiFile(args.midi2)

# Create a new MIDI file to hold the combined tracks
combined = MidiFile()

# Add tracks from the first MIDI file
for i, track in enumerate(midi1.tracks):
    new_track = MidiTrack()
    # Add a Program Change message to set the instrument
    new_track.append(Message('program_change', program=0, time=0))
    for msg in track:
        new_track.append(msg)
    combined.tracks.append(new_track)

# Add tracks from the second MIDI file
for i, track in enumerate(midi2.tracks):
    new_track = MidiTrack()
    # Add a Program Change message to set the instrument
    new_track.append(Message('program_change', program=1, time=0))
    for msg in track:
        new_track.append(msg)
    combined.tracks.append(new_track)

# Save the combined MIDI file
combined.save(args.outfile)

print(f'Combined MIDI files saved as {args.outfile}')
# EXAMPLE: python3 combine_midi.py out/output0.mid ../../data/theChordinator-sample-sequences/163418_23_3_2024_generated_Blues.mid