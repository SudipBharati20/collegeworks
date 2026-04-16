

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JRadioButton;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

class Student {
    protected int id;
    protected String name;
    protected String section;

    public Student(int id, String name, String section) {
        this.id = id;
        this.name = name;
        this.section = section;
    }

    public int getId() {
        return id;
    }

    public String getAddress() {
        return "Address: Kathmandu, Nepal";
    }

    public String getName() {
        return name;
    }

    public String getSection() {
        return section;
    }

    @Override
    public String toString() {
        return id + ", " + name + ", " + section;
    }
}

class BBA extends Student {
    public BBA(int id, String name, String section) {
        super(id, name, section);
    }
}

class BIT extends Student {
    public BIT(int id, String name, String section) {
        super(id, name, section);
    }
}

public class ExceptiondFileHandling {

    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();
        String filename = "students.txt";

        JFrame frame = new JFrame("Student Management System");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(650, 520);
        frame.setLayout(null);

        JLabel idLabel = new JLabel("ID:");
        idLabel.setBounds(50, 50, 100, 30);
        frame.add(idLabel);

        JTextField idField = new JTextField();
        idField.setBounds(150, 50, 150, 30);
        frame.add(idField);

        JLabel nameLabel = new JLabel("Name:");
        nameLabel.setBounds(50, 100, 100, 30);
        frame.add(nameLabel);

        JTextField nameField = new JTextField();
        nameField.setBounds(150, 100, 150, 30);
        frame.add(nameField);

        JRadioButton bbaButton = new JRadioButton("BBA");
        bbaButton.setBounds(50, 150, 100, 30);
        frame.add(bbaButton);

        JRadioButton bitButton = new JRadioButton("BIT");
        bitButton.setBounds(150, 150, 100, 30);
        frame.add(bitButton);

        ButtonGroup group = new ButtonGroup();
        group.add(bbaButton);
        group.add(bitButton);

        JTextArea displayArea = new JTextArea();
        displayArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(displayArea);
        scrollPane.setBounds(350, 50, 260, 380);
        frame.add(scrollPane);

        JButton addButton = new JButton("Add Student");
        addButton.setBounds(50, 220, 150, 30);
        frame.add(addButton);

        JButton displayButton = new JButton("Display Students");
        displayButton.setBounds(50, 270, 150, 30);
        frame.add(displayButton);

        JButton loadButton = new JButton("Load from File");
        loadButton.setBounds(50, 320, 150, 30);
        frame.add(loadButton);

        JButton saveButton = new JButton("Save to File");
        saveButton.setBounds(50, 370, 150, 30);
        frame.add(saveButton);

        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String idText = idField.getText().trim();
                String name = nameField.getText().trim();

                if (idText.isEmpty() || name.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Please enter both ID and Name.", "Input Error", JOptionPane.ERROR_MESSAGE);
                    return;
                }

                if (!bbaButton.isSelected() && !bitButton.isSelected()) {
                    JOptionPane.showMessageDialog(frame, "Please select BBA or BIT.", "Input Error", JOptionPane.ERROR_MESSAGE);
                    return;
                }

                int id;
                try {
                    id = Integer.parseInt(idText);
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame, "ID must be a number.", "Input Error", JOptionPane.ERROR_MESSAGE);
                    return;
                }

                String section = bbaButton.isSelected() ? "BBA" : "BIT";
                Student student = section.equals("BBA") ? new BBA(id, name, section) : new BIT(id, name, section);
                students.add(student);

                JOptionPane.showMessageDialog(frame, "Student added successfully.", "Success", JOptionPane.INFORMATION_MESSAGE);
                idField.setText("");
                nameField.setText("");
                group.clearSelection();
            }
        });

        displayButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (students.isEmpty()) {
                    displayArea.setText("No students available.");
                    return;
                }

                StringBuilder builder = new StringBuilder();
                for (Student student : students) {
                    builder.append(student.toString()).append("\n");
                }
                displayArea.setText(builder.toString());
            }
        });

        saveButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (students.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "No students to save.", "Info", JOptionPane.INFORMATION_MESSAGE);
                    return;
                }

                try (FileWriter writer = new FileWriter(filename)) {
                    for (Student student : students) {
                        writer.write(student.getId() + "," + student.getName() + "," + student.getSection() + "\n");
                    }
                    JOptionPane.showMessageDialog(frame, "Students saved to " + filename, "Saved", JOptionPane.INFORMATION_MESSAGE);
                } catch (IOException ex) {
                    JOptionPane.showMessageDialog(frame, "Error saving file: " + ex.getMessage(), "File Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        loadButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                File file = new File(filename);
                if (!file.exists()) {
                    JOptionPane.showMessageDialog(frame, "File not found: " + filename, "Load Error", JOptionPane.ERROR_MESSAGE);
                    return;
                }

                students.clear();
                try (Scanner scanner = new Scanner(new FileReader(file))) {
                    while (scanner.hasNextLine()) {
                        String line = scanner.nextLine().trim();
                        if (line.isEmpty()) {
                            continue;
                        }
                        String[] parts = line.split(",");
                        if (parts.length != 3) {
                            continue;
                        }
                        int id = Integer.parseInt(parts[0].trim());
                        String name = parts[1].trim();
                        String section = parts[2].trim();

                        if ("BBA".equalsIgnoreCase(section)) {
                            students.add(new BBA(id, name, "BBA"));
                        } else if ("BIT".equalsIgnoreCase(section)) {
                            students.add(new BIT(id, name, "BIT"));
                        } else {
                            students.add(new Student(id, name, section));
                        }
                    }
                    JOptionPane.showMessageDialog(frame, "Students loaded from " + filename, "Loaded", JOptionPane.INFORMATION_MESSAGE);
                    displayButton.doClick();
                } catch (FileNotFoundException ex) {
                    JOptionPane.showMessageDialog(frame, "File not found: " + ex.getMessage(), "Load Error", JOptionPane.ERROR_MESSAGE);
                } catch (Exception ex) {
                    JOptionPane.showMessageDialog(frame, "Error loading file: " + ex.getMessage(), "Load Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        frame.setVisible(true);
    }
}
