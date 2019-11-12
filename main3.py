from lxml import etree

tree = etree.parse("Shout_Description.lsx")

print(tree)

list1 = ["Shout_AS_ResetAp_Description", "Shout_AS_SourceAp_Description", "Shout_RecoverArmour_Description"]

for string in list1:
    if tree.xpath(".//node[@id='TranslatedStringKey']//attribute[@value='{}']".format(string)):
        to_remove = tree.find(".//node[@id='TranslatedStringKey']//attribute[@value='{}']".format(string)).getparent()
        to_remove.getparent().remove(to_remove)

tree.write("out.xml", xml_declaration=True, encoding='utf-8')
